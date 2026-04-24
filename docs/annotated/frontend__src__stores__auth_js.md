# frontend/src/stores/auth.js

## Propósito

Archivo del proyecto ubicado en `frontend/src/stores/auth.js`.

## Código fuente

```js
import { defineStore } from "pinia";
import api from "../api/client";

export const useAuthStore = defineStore("auth", {
  state: () => ({ user: null, token: localStorage.getItem("token") || null }),
  getters: { isAuthenticated: (state) => !!state.token },
  actions: {
    async login(username, password) {
      const form = new URLSearchParams();
      form.append("username", username);
      form.append("password", password);
      const { data } = await api.post("/auth/login", form, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
      });
      this.token = data.access_token;
      this.user = data.user;
      localStorage.setItem("token", data.access_token);
    },
    async fetchMe() {
      if (!this.token) return;
      const { data } = await api.get("/auth/me");
      this.user = data;
    },
    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem("token");
    }
  }
});
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import { defineStore } from "pinia";` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 3 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 4 | `export const useAuthStore = defineStore("auth", {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `  state: () => ({ user: null, token: localStorage.getItem("token") \|\| null }),` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `  getters: { isAuthenticated: (state) => !!state.token },` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `  actions: {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 8 | `    async login(username, password) {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 9 | `      const form = new URLSearchParams();` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `      form.append("username", username);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 11 | `      form.append("password", password);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 12 | `      const { data } = await api.post("/auth/login", form, {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `        headers: { "Content-Type": "application/x-www-form-urlencoded" }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 14 | `      });` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 15 | `      this.token = data.access_token;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `      this.user = data.user;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `      localStorage.setItem("token", data.access_token);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 18 | `    },` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 19 | `    async fetchMe() {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 20 | `      if (!this.token) return;` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 21 | `      const { data } = await api.get("/auth/me");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `      this.user = data;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `    },` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 24 | `    logout() {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 25 | `      this.user = null;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `      this.token = null;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `      localStorage.removeItem("token");` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 28 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 29 | `  }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 30 | `});` | Instrucción de JavaScript/CSS terminada explícitamente. |