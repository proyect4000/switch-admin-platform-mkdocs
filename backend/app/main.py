from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import Base, engine
from app.services.scheduler_service import start_scheduler

from app.models.user import User
from app.models.switch import Switch
from app.models.switch_port import SwitchPort
from app.models.device_link import DeviceLink
from app.models.device_neighbor import DeviceNeighbor
from app.models.discovery_run import DiscoveryRun
from app.models.ssh_session import SSHSession
from app.models.ssh_command import SSHCommand
from app.models.audit_log import AuditLog
from app.models.config_backup import ConfigBackup
from app.models.scheduled_job import ScheduledJob

from app.api.v1 import auth, switches, ports, topology, history, discovery, backups, reports, dashboard, jobs, users, roles, websocket_ssh

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Auth"])
app.include_router(switches.router, prefix=f"{settings.API_V1_STR}/switches", tags=["Switches"])
app.include_router(ports.router, prefix=f"{settings.API_V1_STR}/ports", tags=["Ports"])
app.include_router(topology.router, prefix=f"{settings.API_V1_STR}/topology", tags=["Topology"])
app.include_router(history.router, prefix=f"{settings.API_V1_STR}/history", tags=["History"])
app.include_router(discovery.router, prefix=f"{settings.API_V1_STR}/discovery", tags=["Discovery"])
app.include_router(backups.router, prefix=f"{settings.API_V1_STR}/backups", tags=["Backups"])
app.include_router(reports.router, prefix=f"{settings.API_V1_STR}/reports", tags=["Reports"])
app.include_router(dashboard.router, prefix=f"{settings.API_V1_STR}/dashboard", tags=["Dashboard"])
app.include_router(jobs.router, prefix=f"{settings.API_V1_STR}/jobs", tags=["Jobs"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Users"])
app.include_router(roles.router, prefix=f"{settings.API_V1_STR}/roles", tags=["Roles"])
app.include_router(websocket_ssh.router, tags=["WebSocket SSH"])

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/")
def root():
    return {"message": "Switch Admin Platform API"}
