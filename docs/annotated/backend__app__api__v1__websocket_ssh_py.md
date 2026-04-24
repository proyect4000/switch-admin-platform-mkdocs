# backend/app/api/v1/websocket_ssh.py

## Propósito

Archivo del proyecto ubicado en `backend/app/api/v1/websocket_ssh.py`.

## Código fuente

```py
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
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import asyncio` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `import uuid` | Importa un módulo o paquete necesario para este archivo. |
| 3 | `from datetime import datetime` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 4 | `from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from sqlalchemy.orm import Session` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 7 | `from app.core.database import SessionLocal` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 8 | `from app.core.security import decode_access_token` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.models.user import User` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 11 | `from app.models.ssh_session import SSHSession` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 12 | `from app.models.ssh_command import SSHCommand` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 13 | `from app.services.ssh_service import SSHService` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 14 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 15 | `router = APIRouter()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 17 | `@router.websocket("/ws/ssh/{switch_id}")` | Decorador de FastAPI que registra una ruta o endpoint en la API. |
| 18 | `async def websocket_ssh(websocket: WebSocket, switch_id: int, token: str = Query(...)):` | Declara la función asíncrona `websocket_ssh` para operaciones no bloqueantes, como WebSocket o I/O. |
| 19 | `    db: Session = SessionLocal()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `    client = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    channel = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `    session_row = None` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `    try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 24 | `        payload = decode_access_token(token)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `        if not payload:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 26 | `            await websocket.close(code=1008)` | Espera el resultado de una operación asíncrona antes de continuar. |
| 27 | `            return` | Finaliza la función sin devolver un valor explícito. |
| 28 | `        username = payload.get("sub")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `        user = db.query(User).filter(User.username == username).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 30 | `        if not user:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 31 | `            await websocket.close(code=1008)` | Espera el resultado de una operación asíncrona antes de continuar. |
| 32 | `            return` | Finaliza la función sin devolver un valor explícito. |
| 33 | `        switch = db.query(Switch).filter(Switch.id == switch_id, Switch.is_deleted == False).first()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `        if not switch:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 35 | `            await websocket.accept()` | Espera el resultado de una operación asíncrona antes de continuar. |
| 36 | `            await websocket.send_text("\r\n[ERROR] Switch no encontrado\r\n")` | Espera el resultado de una operación asíncrona antes de continuar. |
| 37 | `            await websocket.close()` | Espera el resultado de una operación asíncrona antes de continuar. |
| 38 | `            return` | Finaliza la función sin devolver un valor explícito. |
| 39 | `        await websocket.accept()` | Espera el resultado de una operación asíncrona antes de continuar. |
| 40 | `        client = SSHService._connect(switch.ip_address, switch.ssh_port, switch.ssh_username, switch.ssh_password_encrypted)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 41 | `        channel = client.invoke_shell()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 42 | `        session_row = SSHSession(` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 43 | `            user_id=user.id, switch_id=switch.id, session_uuid=str(uuid.uuid4()),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `            client_ip=websocket.client.host if websocket.client else None, status="open"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 45 | `        )` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 46 | `        db.add(session_row); db.commit(); db.refresh(session_row)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 47 | `        await websocket.send_text(f"\r\nConectado a {switch.name} ({switch.ip_address})\r\n")` | Espera el resultado de una operación asíncrona antes de continuar. |
| 48 | `        while True:` | Inicia un ciclo que se repetirá mientras la condición sea verdadera. |
| 49 | `            if channel.recv_ready():` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 50 | `                output = channel.recv(8192).decode("utf-8", errors="ignore")` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 51 | `                await websocket.send_text(output)` | Espera el resultado de una operación asíncrona antes de continuar. |
| 52 | `            try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 53 | `                data = await asyncio.wait_for(websocket.receive_text(), timeout=0.1)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 54 | `                channel.send(data)` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 55 | `                db.add(SSHCommand(session_id=session_row.id, command_text=data, output_text=None, success=True))` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 56 | `                db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 57 | `            except asyncio.TimeoutError:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 58 | `                continue` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 59 | `            except WebSocketDisconnect:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 60 | `                break` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 61 | `    finally:` | Bloque de cierre que se ejecuta siempre, útil para liberar recursos. |
| 62 | `        try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 63 | `            if session_row:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 64 | `                session_row.status = "closed"` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 65 | `                session_row.ended_at = datetime.utcnow()` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 66 | `                db.commit()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 67 | `        except Exception:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 68 | `            pass` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 69 | `        try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 70 | `            if channel:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 71 | `                channel.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 72 | `        except Exception:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 73 | `            pass` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 74 | `        try:` | Inicio del manejo controlado de errores para operaciones riesgosas. |
| 75 | `            if client:` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 76 | `                client.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 77 | `        except Exception:` | Captura una excepción específica para responder sin interrumpir toda la aplicación. |
| 78 | `            pass` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 79 | `        db.close()` | Línea de implementación que forma parte del comportamiento interno del archivo. |