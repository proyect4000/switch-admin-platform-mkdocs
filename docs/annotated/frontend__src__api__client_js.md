# frontend/src/api/client.js

## Propósito

Archivo del proyecto ubicado en `frontend/src/api/client.js`.

## Código fuente

```js
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1"
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import axios from "axios";` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 3 | `const api = axios.create({` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 4 | `  baseURL: import.meta.env.VITE_API_URL \|\| "http://localhost:8000/api/v1"` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 5 | `});` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 6 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 7 | `api.interceptors.request.use((config) => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `  const token = localStorage.getItem("token");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `  if (token) config.headers.Authorization = \`Bearer ${token}\`;` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 10 | `  return config;` | Devuelve el resultado de la función al código que la llamó. |
| 11 | `});` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 12 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 13 | `export default api;` | Instrucción de JavaScript/CSS terminada explícitamente. |