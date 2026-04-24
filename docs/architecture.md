# Arquitectura del sistema

## Backend

El backend usa FastAPI para exponer una API REST y un canal WebSocket para la consola SSH.

### Capas principales

- `api/v1`: rutas HTTP y WebSocket
- `core`: configuración, seguridad, cifrado y conexión a base de datos
- `models`: entidades SQLAlchemy
- `schemas`: contratos Pydantic
- `services`: lógica de negocio
- `parsers`: análisis de salida CLI por fabricante
- `utils`: utilitarios auxiliares

## Frontend

El frontend usa Vue 3 con Vite.

### Áreas funcionales

- Autenticación
- Dashboard
- Gestión de switches
- Topología
- Vecinos
- Backups
- Tareas programadas
- Historial

## Base de datos

PostgreSQL guarda usuarios, switches, puertos, enlaces, sesiones SSH, comandos, discoveries, backups y jobs programados.
