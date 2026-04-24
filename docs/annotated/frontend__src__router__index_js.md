# frontend/src/router/index.js

## Propósito

Archivo del proyecto ubicado en `frontend/src/router/index.js`.

## Código fuente

```js
import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import DashboardView from "../views/DashboardView.vue";
import SwitchesView from "../views/SwitchesView.vue";
import TopologyView from "../views/TopologyView.vue";
import HistoryView from "../views/HistoryView.vue";
import NeighborsView from "../views/NeighborsView.vue";
import BackupsView from "../views/BackupsView.vue";
import JobsView from "../views/JobsView.vue";

const routes = [
  { path: "/login", component: LoginView },
  { path: "/", redirect: "/dashboard" },
  { path: "/dashboard", component: DashboardView },
  { path: "/switches", component: SwitchesView },
  { path: "/topology", component: TopologyView },
  { path: "/history", component: HistoryView },
  { path: "/neighbors", component: NeighborsView },
  { path: "/backups", component: BackupsView },
  { path: "/jobs", component: JobsView }
];

const router = createRouter({ history: createWebHistory(), routes });

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");
  if (to.path !== "/login" && !token) next("/login");
  else if (to.path === "/login" && token) next("/dashboard");
  else next();
});

export default router;
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `import { createRouter, createWebHistory } from "vue-router";` | Importa un módulo o paquete necesario para este archivo. |
| 2 | `import LoginView from "../views/LoginView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 3 | `import DashboardView from "../views/DashboardView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 4 | `import SwitchesView from "../views/SwitchesView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 5 | `import TopologyView from "../views/TopologyView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 6 | `import HistoryView from "../views/HistoryView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 7 | `import NeighborsView from "../views/NeighborsView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 8 | `import BackupsView from "../views/BackupsView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 9 | `import JobsView from "../views/JobsView.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `const routes = [` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `  { path: "/login", component: LoginView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 13 | `  { path: "/", redirect: "/dashboard" },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 14 | `  { path: "/dashboard", component: DashboardView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 15 | `  { path: "/switches", component: SwitchesView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 16 | `  { path: "/topology", component: TopologyView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 17 | `  { path: "/history", component: HistoryView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 18 | `  { path: "/neighbors", component: NeighborsView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 19 | `  { path: "/backups", component: BackupsView },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 20 | `  { path: "/jobs", component: JobsView }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 21 | `];` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 22 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 23 | `const router = createRouter({ history: createWebHistory(), routes });` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 25 | `router.beforeEach((to, from, next) => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `  const token = localStorage.getItem("token");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `  if (to.path !== "/login" && !token) next("/login");` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 28 | `  else if (to.path === "/login" && token) next("/dashboard");` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 29 | `  else next();` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 30 | `});` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 31 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 32 | `export default router;` | Instrucción de JavaScript/CSS terminada explícitamente. |