# backend/app/main.py

## Propósito

Archivo del proyecto ubicado en `backend/app/main.py`.

## Código fuente

```py
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

from app.api.v1 import auth, switches, ports, topology, history, discovery, backups, reports, dashboard, jobs, websocket_ssh

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
app.include_router(websocket_ssh.router, tags=["WebSocket SSH"])

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/")
def root():
    return {"message": "Switch Admin Platform API"}
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `from fastapi import FastAPI` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 2 | `from fastapi.middleware.cors import CORSMiddleware` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `from app.core.config import settings` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 5 | `from app.core.database import Base, engine` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 6 | `from app.services.scheduler_service import start_scheduler` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 7 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 8 | `from app.models.user import User` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 9 | `from app.models.switch import Switch` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 10 | `from app.models.switch_port import SwitchPort` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 11 | `from app.models.device_link import DeviceLink` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 12 | `from app.models.device_neighbor import DeviceNeighbor` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 13 | `from app.models.discovery_run import DiscoveryRun` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 14 | `from app.models.ssh_session import SSHSession` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 15 | `from app.models.ssh_command import SSHCommand` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 16 | `from app.models.audit_log import AuditLog` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 17 | `from app.models.config_backup import ConfigBackup` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 18 | `from app.models.scheduled_job import ScheduledJob` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 19 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 20 | `from app.api.v1 import auth, switches, ports, topology, history, discovery, backups, reports, dashboard, jobs, websocket_ssh` | Importa nombres específicos desde otro módulo para reutilizar lógica o tipos. |
| 21 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 22 | `Base.metadata.create_all(bind=engine)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 24 | `app = FastAPI(title=settings.APP_NAME)` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 26 | `app.add_middleware(` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `    CORSMiddleware,` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `    allow_origins=[settings.FRONTEND_ORIGIN],` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `    allow_credentials=True,` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `    allow_methods=["*"],` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `    allow_headers=["*"],` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `)` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 33 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 34 | `app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Auth"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 35 | `app.include_router(switches.router, prefix=f"{settings.API_V1_STR}/switches", tags=["Switches"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 36 | `app.include_router(ports.router, prefix=f"{settings.API_V1_STR}/ports", tags=["Ports"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 37 | `app.include_router(topology.router, prefix=f"{settings.API_V1_STR}/topology", tags=["Topology"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 38 | `app.include_router(history.router, prefix=f"{settings.API_V1_STR}/history", tags=["History"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 39 | `app.include_router(discovery.router, prefix=f"{settings.API_V1_STR}/discovery", tags=["Discovery"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 40 | `app.include_router(backups.router, prefix=f"{settings.API_V1_STR}/backups", tags=["Backups"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 41 | `app.include_router(reports.router, prefix=f"{settings.API_V1_STR}/reports", tags=["Reports"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 42 | `app.include_router(dashboard.router, prefix=f"{settings.API_V1_STR}/dashboard", tags=["Dashboard"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 43 | `app.include_router(jobs.router, prefix=f"{settings.API_V1_STR}/jobs", tags=["Jobs"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `app.include_router(websocket_ssh.router, tags=["WebSocket SSH"])` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 45 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 46 | `@app.on_event("startup")` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 47 | `def startup_event():` | Declara la función `startup_event` con la lógica que se ejecutará cuando sea invocada. |
| 48 | `    start_scheduler()` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 49 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 50 | `@app.get("/")` | Decorador que modifica o registra el comportamiento del elemento definido a continuación. |
| 51 | `def root():` | Declara la función `root` con la lógica que se ejecutará cuando sea invocada. |
| 52 | `    return {"message": "Switch Admin Platform API"}` | Devuelve el resultado de la función al código que la llamó. |