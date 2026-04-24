import asyncio
import uuid
from datetime import datetime
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.security import decode_access_token
from app.models.user import User
from app.models.switch import Switch
from app.models.ssh_session import SSHSession
from app.models.ssh_command import SSHCommand
from app.services.ssh_service import SSHService

router = APIRouter()

@router.websocket("/ws/ssh/{switch_id}")
async def websocket_ssh(websocket: WebSocket, switch_id: int, token: str = Query(...)):
    db: Session = SessionLocal()
    client = None
    channel = None
    session_row = None
    try:
        payload = decode_access_token(token)
        if not payload:
            await websocket.close(code=1008)
            return
        username = payload.get("sub")
        user = db.query(User).filter(User.username == username).first()
        if not user:
            await websocket.close(code=1008)
            return
        switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()
        if not switch:
            await websocket.accept()
            await websocket.send_text("\r\n[ERROR] Switch no encontrado\r\n")
            await websocket.close()
            return
        await websocket.accept()
        client = SSHService._connect(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted)
        channel = client.invoke_shell()
        session_row = SSHSession(
            user_id=user.id, switch_id=switch.id, session_uuid=str(uuid.uuid4()),
            client_ip=websocket.client.host if websocket.client else None, status="open"
        )
        db.add(session_row); db.commit(); db.refresh(session_row)
        await websocket.send_text(f"\r\nConectado a {switch.name} ({switch.ip_address})\r\n")
        while True:
            if channel.recv_ready():
                output = channel.recv(8192).decode("utf-8", errors="ignore")
                await websocket.send_text(output)
            try:
                data = await asyncio.wait_for(websocket.receive_text(), timeout=0.1)
                channel.send(data)
                db.add(SSHCommand(session_id=session_row.id, command_text=data, output_text=None, success=True))
                db.commit()
            except asyncio.TimeoutError:
                continue
            except WebSocketDisconnect:
                break
    finally:
        try:
            if session_row:
                session_row.status = "closed"
                session_row.ended_at = datetime.utcnow()
                db.commit()
        except Exception:
            pass
        try:
            if channel:
                channel.close()
        except Exception:
            pass
        try:
            if client:
                client.close()
        except Exception:
            pass
        db.close()
