# Guía paso a paso - Ubuntu Server 24.04

## 1. Preparar servidor
```bash
sudo apt update && sudo apt upgrade -y
sudo timedatectl set-timezone America/Lima
sudo apt install -y curl git unzip ufw
```

## 2. Instalar Docker
```bash
sudo apt install -y docker.io docker-compose-v2
sudo systemctl enable docker
sudo systemctl start docker
docker --version
docker compose version
```

## 3. Copiar proyecto
```bash
sudo mkdir -p /opt/switch-admin-platform
sudo chown $USER:$USER /opt/switch-admin-platform
cd /opt/switch-admin-platform
```
Copiar el contenido del proyecto descargado dentro de esta ruta.

## 4. Ajustar variables
### Backend
Editar `backend/.env`
- SECRET_KEY
- SSH_SECRET_KEY
- FRONTEND_ORIGIN

### Frontend
Editar `frontend/.env`
- VITE_API_URL
- VITE_WS_URL

## 5. Levantar contenedores
```bash
cd /opt/switch-admin-platform
docker compose up --build -d
docker ps
```

## 6. Crear administrador inicial
```bash
docker exec -it switch-backend python create_admin.py
```

## 7. Acceder
- Frontend: `http://IP_SERVIDOR:5173`
- API: `http://IP_SERVIDOR:8000/docs`

## 8. Apertura de puertos UFW
```bash
sudo ufw allow 22/tcp
sudo ufw allow 5173/tcp
sudo ufw allow 8000/tcp
sudo ufw enable
sudo ufw status
```

## 9. Operación básica
1. Ingresar con `admin / Admin123*`
2. Registrar un switch
3. Probar SSH
4. Ejecutar discovery
5. Ver topología
6. Abrir consola SSH
7. Generar backup
8. Crear tarea programada

## 10. Recomendaciones
- Cambiar credenciales por defecto después del primer ingreso.
- No exponer PostgreSQL a Internet.
- Implementar Nginx con HTTPS para producción.
- Ajustar parsers según la marca real de los switches.
