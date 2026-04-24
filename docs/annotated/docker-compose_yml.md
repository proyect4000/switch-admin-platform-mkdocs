# docker-compose.yml

## Propósito

Archivo del proyecto ubicado en `docker-compose.yml`.

## Código fuente

```yaml
version: "3.9"

services:
  db:
    image: postgres:16
    container_name: switchdb
    restart: always
    environment:
      POSTGRES_DB: switchdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./backend
    container_name: switch-backend
    restart: always
    depends_on:
      - db
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    container_name: switch-frontend
    restart: always
    depends_on:
      - backend
    ports:
      - "5173:80"

volumes:
  postgres_data:
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `version: "3.9"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `services:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 4 | `  db:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 5 | `    image: postgres:16` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    container_name: switchdb` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 7 | `    restart: always` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `    environment:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 9 | `      POSTGRES_DB: switchdb` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 10 | `      POSTGRES_USER: postgres` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 11 | `      POSTGRES_PASSWORD: postgres` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 12 | `    ports:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 13 | `      - "5432:5432"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `    volumes:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `      - postgres_data:/var/lib/postgresql/data` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 16 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 17 | `  backend:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 18 | `    build: ./backend` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `    container_name: switch-backend` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 20 | `    restart: always` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `    depends_on:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 22 | `      - db` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 23 | `    ports:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 24 | `      - "8000:8000"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 25 | `    env_file:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 26 | `      - ./backend/.env` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 27 | `    volumes:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 28 | `      - ./backend:/app` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 29 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 30 | `  frontend:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 31 | `    build: ./frontend` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 32 | `    container_name: switch-frontend` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 33 | `    restart: always` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 34 | `    depends_on:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 35 | `      - backend` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 36 | `    ports:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 37 | `      - "5173:80"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 38 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 39 | `volumes:` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 40 | `  postgres_data:` | Línea de implementación que forma parte del comportamiento interno del archivo. |