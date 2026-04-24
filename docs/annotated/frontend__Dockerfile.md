# frontend/Dockerfile

## Propósito

Archivo del proyecto ubicado en `frontend/Dockerfile`.

## Código fuente

```dockerfile
FROM node:20 AS build

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `FROM node:20 AS build` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `WORKDIR /app` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 4 | `COPY package*.json ./` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 5 | `RUN npm install` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 6 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 7 | `COPY . .` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 8 | `RUN npm run build` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 9 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 10 | `FROM nginx:stable-alpine` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 11 | `COPY --from=build /app/dist /usr/share/nginx/html` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `COPY nginx.conf /etc/nginx/conf.d/default.conf` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 13 | `EXPOSE 80` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `CMD ["nginx", "-g", "daemon off;"]` | Línea de implementación que forma parte del comportamiento interno del archivo. |