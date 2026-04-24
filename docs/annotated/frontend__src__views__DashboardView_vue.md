# frontend/src/views/DashboardView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/DashboardView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Dashboard Ejecutivo</div>
      <div class="grid grid-3">
        <div class="card"><h3>Total de switches</h3><p>{{ summary.total_switches }}</p></div>
        <div class="card"><h3>Switches online</h3><p>{{ summary.online_switches }}</p></div>
        <div class="card"><h3>Switches offline</h3><p>{{ summary.offline_switches }}</p></div>
        <div class="card"><h3>Discovery OK</h3><p>{{ summary.discovery_success }}</p></div>
        <div class="card"><h3>Discovery error</h3><p>{{ summary.discovery_error }}</p></div>
        <div class="card"><h3>Total backups</h3><p>{{ summary.backups_total }}</p></div>
      </div>
      <div class="card" style="margin-top:16px;">
        <div class="toolbar">
          <a :href="`${apiBase}/reports/switches.csv`" target="_blank"><button class="secondary">Exportar switches CSV</button></a>
        </div>
        <p>Panel general del estado del sistema, descubrimientos, backups y accesos rápidos.</p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, reactive } from "vue";
import api from "../api/client";
import AppSidebar from "../components/AppSidebar.vue";
const apiBase = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";
const summary = reactive({ total_switches:0, online_switches:0, offline_switches:0, discovery_success:0, discovery_error:0, backups_total:0 });
const loadSummary = async () => { const { data } = await api.get("/dashboard/summary"); Object.assign(summary, data); };
onMounted(loadSummary);
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Dashboard Ejecutivo</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="grid grid-3">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <div class="card"><h3>Total de switches</h3><p>{{ summary.total_switches }}</p></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `        <div class="card"><h3>Switches online</h3><p>{{ summary.online_switches }}</p></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `        <div class="card"><h3>Switches offline</h3><p>{{ summary.offline_switches }}</p></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `        <div class="card"><h3>Discovery OK</h3><p>{{ summary.discovery_success }}</p></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        <div class="card"><h3>Discovery error</h3><p>{{ summary.discovery_error }}</p></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `        <div class="card"><h3>Total backups</h3><p>{{ summary.backups_total }}</p></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 14 | `      <div class="card" style="margin-top:16px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `        <div class="toolbar">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `          <a :href="\`${apiBase}/reports/switches.csv\`" target="_blank"><button class="secondary">Exportar switches CSV</button></a>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 18 | `        <p>Panel general del estado del sistema, descubrimientos, backups y accesos rápidos.</p>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 19 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 20 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 21 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 22 | `</template>` | Fin del bloque de plantilla de Vue. |
| 23 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 24 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 25 | `import { onMounted, reactive } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 26 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 27 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 28 | `const apiBase = import.meta.env.VITE_API_URL \|\| "http://localhost:8000/api/v1";` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `const summary = reactive({ total_switches:0, online_switches:0, offline_switches:0, discovery_success:0, discovery_error:0, backups_total...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `const loadSummary = async () => { const { data } = await api.get("/dashboard/summary"); Object.assign(summary, data); };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `onMounted(loadSummary);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 32 | `</script>` | Fin del bloque de lógica del componente Vue. |