# Documentación técnica del proyecto  
## Switch Admin Platform

### 1. Resumen ejecutivo
Switch Admin Platform es una aplicación web empresarial para registrar, administrar y operar switches de red mediante conexión SSH. El sistema permite centralizar el inventario técnico, validar conectividad SSH, ejecutar sesiones desde navegador, descubrir puertos y vecinos, visualizar la topología en mapa, generar backups de configuración, programar tareas automáticas y mantener trazabilidad mediante historial y auditoría.

### 2. Objetivos
- Centralizar la administración de switches en una sola plataforma web.
- Mejorar la trazabilidad de accesos y cambios realizados.
- Reducir el trabajo manual en descubrimiento de topología.
- Facilitar respaldo de configuraciones y operación diaria.

### 3. Arquitectura
#### 3.1 Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Paramiko
- APScheduler

#### 3.2 Frontend
- Vue 3
- Vite
- Pinia
- Axios
- vis-network
- xterm.js

#### 3.3 Comunicación
- REST para operaciones de negocio
- WebSocket para consola SSH

### 4. Módulos
- Autenticación y roles
- Gestión de switches
- Gestión de puertos
- Discovery automático
- Topología
- Consola SSH
- Backups
- Jobs programados
- Historial y auditoría
- Reportes

### 5. Modelo de datos
Principales entidades:
- users
- switches
- switch_ports
- device_links
- device_neighbors
- discovery_runs
- ssh_sessions
- ssh_commands
- config_backups
- scheduled_jobs
- audit_logs

### 6. Flujo del sistema
1. El administrador inicia sesión.
2. Registra un switch con IP y credenciales.
3. Ejecuta prueba SSH.
4. Lanza discovery para leer interfaces y vecinos.
5. El sistema actualiza puertos y enlaces.
6. La topología refleja el estado detectado.
7. Se puede abrir consola SSH desde la web.
8. Se generan backups y se programan tareas.
9. Todo queda auditado.

### 7. Estructura de carpetas
Ver paquete descargable del proyecto.

### 8. Endpoints principales
- POST /api/v1/auth/login
- GET /api/v1/auth/me
- GET /api/v1/switches
- POST /api/v1/switches
- PUT /api/v1/switches/{id}
- DELETE /api/v1/switches/{id}
- POST /api/v1/switches/{id}/test-ssh
- POST /api/v1/discovery/switches/{id}/run
- GET /api/v1/discovery/switches/{id}/neighbors
- POST /api/v1/backups/switches/{id}/run
- GET /api/v1/backups/switches/{id}
- GET /api/v1/dashboard/summary
- GET /api/v1/jobs
- POST /api/v1/jobs
- WS /ws/ssh/{switch_id}

### 9. Seguridad
- JWT Bearer
- Roles y permisos
- Cifrado de credenciales SSH
- Auditoría de acciones
- Recomendación de validación estricta de host keys

### 10. Despliegue
El despliegue recomendado es Ubuntu Server 24.04 con Docker Compose. Se incluye archivo README_DEPLOY.md con el paso a paso.

### 11. Recomendaciones para producción
- Añadir Alembic para migraciones.
- Ajustar parsers por marca/modelo.
- Añadir reverse proxy con HTTPS.
- Restringir CORS al dominio final.
- Implementar descarga directa de backup como archivo.
- Integrar monitoreo y logs centralizados.

### 12. Conclusión
El proyecto entregado constituye una base funcional avanzada para iniciar una implementación institucional o empresarial. Antes de producción se recomienda una fase de pruebas con switches reales y afinamiento por fabricante.
