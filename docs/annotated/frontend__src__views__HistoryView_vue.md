# frontend/src/views/HistoryView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/HistoryView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Historial y auditoría</div>
      <div class="grid grid-2">
        <div class="card"><h3>Sesiones SSH</h3><div class="table-wrapper"><table><thead><tr><th>ID</th><th>Switch</th><th>Cliente</th><th>Estado</th><th>Inicio</th></tr></thead><tbody><tr v-for="item in sessions" :key="item.id"><td>{{ item.id }}</td><td>{{ item.switch_id }}</td><td>{{ item.client_ip }}</td><td>{{ item.status }}</td><td>{{ item.started_at }}</td></tr></tbody></table></div></div>
        <div class="card"><h3>Auditoría</h3><div class="table-wrapper"><table><thead><tr><th>ID</th><th>Acción</th><th>Entidad</th><th>Detalle</th><th>Fecha</th></tr></thead><tbody><tr v-for="item in auditLogs" :key="item.id"><td>{{ item.id }}</td><td>{{ item.action }}</td><td>{{ item.entity_type }}</td><td>{{ item.detail }}</td><td>{{ item.created_at }}</td></tr></tbody></table></div></div>
      </div>
      <div class="card" style="margin-top:16px;"><h3>Comandos SSH</h3><div class="table-wrapper"><table><thead><tr><th>ID</th><th>Sesión</th><th>Comando</th><th>Fecha</th></tr></thead><tbody><tr v-for="item in commands" :key="item.id"><td>{{ item.id }}</td><td>{{ item.session_id }}</td><td>{{ item.command_text }}</td><td>{{ item.executed_at }}</td></tr></tbody></table></div></div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../api/client";
import AppSidebar from "../components/AppSidebar.vue";
const sessions = ref([]), commands = ref([]), auditLogs = ref([]);
const loadHistory = async () => {
  sessions.value = (await api.get("/history/sessions")).data;
  commands.value = (await api.get("/history/commands")).data;
  auditLogs.value = (await api.get("/history/audit-logs")).data;
};
onMounted(loadHistory);
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Historial y auditoría</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="grid grid-2">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <div class="card"><h3>Sesiones SSH</h3><div class="table-wrapper"><table><thead><tr><th>ID</th><th>Switch</th><th>Cliente</th><th...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `        <div class="card"><h3>Auditoría</h3><div class="table-wrapper"><table><thead><tr><th>ID</th><th>Acción</th><th>Entidad</th><th>De...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 10 | `      <div class="card" style="margin-top:16px;"><h3>Comandos SSH</h3><div class="table-wrapper"><table><thead><tr><th>ID</th><th>Sesión<...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 12 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 13 | `</template>` | Fin del bloque de plantilla de Vue. |
| 14 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 15 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 16 | `import { onMounted, ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 17 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 18 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 19 | `const sessions = ref([]), commands = ref([]), auditLogs = ref([]);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `const loadHistory = async () => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `  sessions.value = (await api.get("/history/sessions")).data;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `  commands.value = (await api.get("/history/commands")).data;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `  auditLogs.value = (await api.get("/history/audit-logs")).data;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `};` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 25 | `onMounted(loadHistory);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 26 | `</script>` | Fin del bloque de lógica del componente Vue. |