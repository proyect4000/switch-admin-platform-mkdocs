# backend/Dockerfile

## Propósito

Archivo del proyecto ubicado en `backend/Dockerfile`.

## Código fuente

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential gcc libpq-dev openssh-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `FROM python:3.12-slim` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `WORKDIR /app` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 4 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 5 | `RUN apt-get update && apt-get install -y \` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `    build-essential gcc libpq-dev openssh-client \` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 7 | `    && rm -rf /var/lib/apt/lists/*` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 9 | `COPY requirements.txt .` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 10 | `RUN pip install --no-cache-dir -r requirements.txt` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 11 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 12 | `COPY . .` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 13 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 14 | `EXPOSE 8000` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 15 | `CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]` | Línea de implementación que forma parte del comportamiento interno del archivo. |