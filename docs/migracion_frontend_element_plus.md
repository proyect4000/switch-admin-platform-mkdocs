# Migración del Frontend a Vue Element Plus Admin

Esta versión reemplaza el frontend básico por la plantilla `vue-element-plus-admin`, basada en Vue 3, Vite, TypeScript, Pinia, Vue Router 4 y Element Plus.

## Módulos migrados

- Dashboard Ejecutivo
- Gestión de Switches
- Topología con `vis-network`
- Vecinos LLDP/CDP
- Backups de configuración
- Tareas programadas
- Historial y auditoría
- Usuarios
- Roles y permisos
- Consola SSH con `@xterm/xterm`

## Backend actualizado

Se corrigió la compatibilidad con Pydantic v2:

```python
from pydantic_settings import BaseSettings
```

También se agregó en `backend/requirements.txt`:

```txt
pydantic-settings
bcrypt==4.0.1
```

## Roles disponibles

- `superadmin`: acceso total.
- `admin`: administra usuarios, switches, backups, reportes y auditoría.
- `operator`: puede operar SSH, discovery y visualizar backups.
- `viewer`: solo lectura básica e historial autorizado.

## Usuario inicial

```bash
docker exec -it switch-backend python create_admin.py
```

Credenciales iniciales:

- Usuario: `admin`
- Contraseña: `Admin123*`
