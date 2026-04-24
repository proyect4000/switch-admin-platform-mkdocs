# SWITCH ADMIN PLATFORM

Sistema web para administración de switches por SSH, topología, discovery, backups y auditoría.

## 1. Características

- Autenticación JWT y roles.
- CRUD de switches.
- Prueba SSH.
- Descubrimiento automático de puertos y vecinos.
- Topología visual.
- Consola SSH en navegador.
- Backups de configuración.
- Tareas programadas.
- Historial y auditoría.
- Exportación CSV.

## 2. Arquitectura

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Paramiko
- APScheduler

### Frontend
- Vue 3
- Vite
- Pinia
- Axios
- vis-network
- xterm.js

## 3. Instalación rápida

### Requisitos
- Ubuntu Server 24.04
- Docker
- Docker Compose v2

### Levantar servicios
```bash
cd /opt/switch-admin-platform
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
docker compose up --build -d
```

### Crear administrador
```bash
docker exec -it switch-backend python create_admin.py
```

### Accesos
- Frontend: `http://IP_SERVIDOR:5173`
- Backend docs: `http://IP_SERVIDOR:8000/docs`

## 4. Flujo recomendado

1. Iniciar sesión con admin.
2. Registrar switches.
3. Ejecutar prueba SSH.
4. Lanzar discovery.
5. Ver topología.
6. Abrir consola SSH.
7. Generar backups.
8. Crear tareas programadas.

## 5. Seguridad recomendada

- Cambiar `SECRET_KEY`.
- Cambiar `SSH_SECRET_KEY`.
- No exponer PostgreSQL a internet.
- Usar HTTPS con reverse proxy.
- Restringir acceso por firewall.
- Cargar host keys reales de los switches.

## 6. Limitaciones actuales

- Los parsers LLDP/CDP están preparados como base y pueden requerir ajuste fino por fabricante/modelo.
- Las tablas se crean automáticamente desde SQLAlchemy; para producción estricta conviene migrar a Alembic.
- El proyecto es una base funcional avanzada, pero necesita pruebas con tus equipos reales antes de producción.
