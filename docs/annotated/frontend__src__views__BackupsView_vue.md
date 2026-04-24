# frontend/src/views/BackupsView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/BackupsView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Backups de configuración</div>
      <div class="card" style="margin-bottom:16px;">
        <div class="toolbar">
          <input v-model="switchId" placeholder="ID del switch" style="max-width:200px;" />
          <button @click="loadBackups">Consultar backups</button>
          <button class="success" @click="runBackup">Generar backup</button>
        </div>
      </div>
      <div class="card table-wrapper">
        <table>
          <thead><tr><th>ID</th><th>Switch</th><th>Tipo</th><th>Archivo</th><th>Fecha</th><th>Acción</th></tr></thead>
          <tbody><tr v-for="item in backups" :key="item.id"><td>{{ item.id }}</td><td>{{ item.switch_id }}</td><td>{{ item.backup_type }}</td><td>{{ item.filename }}</td><td>{{ item.created_at }}</td><td><button class="secondary" @click="viewBackup(item.id)">Ver contenido</button></td></tr></tbody>
        </table>
      </div>
      <div v-if="selectedBackup" class="card" style="margin-top:16px;">
        <h3>Contenido del backup</h3>
        <pre style="background:#0f172a;color:#e2e8f0;padding:16px;border-radius:10px;overflow:auto;max-height:500px;white-space:pre-wrap;">{{ selectedBackup.content }}</pre>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "../api/client";
import AppSidebar from "../components/AppSidebar.vue";
const switchId = ref(""), backups = ref([]), selectedBackup = ref(null);
const loadBackups = async () => { if (!switchId.value) return; backups.value = (await api.get(`/backups/switches/${switchId.value}`)).data; selectedBackup.value = null; };
const runBackup = async () => { if (!switchId.value) return; await api.post(`/backups/switches/${switchId.value}/run?backup_type=running-config`); await loadBackups(); };
const viewBackup = async (backupId) => { selectedBackup.value = (await api.get(`/backups/${backupId}`)).data; };
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Backups de configuración</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="card" style="margin-bottom:16px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <div class="toolbar">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `          <input v-model="switchId" placeholder="ID del switch" style="max-width:200px;" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `          <button @click="loadBackups">Consultar backups</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `          <button class="success" @click="runBackup">Generar backup</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 12 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 13 | `      <div class="card table-wrapper">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `        <table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 15 | `          <thead><tr><th>ID</th><th>Switch</th><th>Tipo</th><th>Archivo</th><th>Fecha</th><th>Acción</th></tr></thead>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 16 | `          <tbody><tr v-for="item in backups" :key="item.id"><td>{{ item.id }}</td><td>{{ item.switch_id }}</td><td>{{ item.backup_type }}...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `        </table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 18 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 19 | `      <div v-if="selectedBackup" class="card" style="margin-top:16px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `        <h3>Contenido del backup</h3>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 21 | `        <pre style="background:#0f172a;color:#e2e8f0;padding:16px;border-radius:10px;overflow:auto;max-height:500px;white-space:pre-wrap;...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 23 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 24 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 25 | `</template>` | Fin del bloque de plantilla de Vue. |
| 26 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 27 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 28 | `import { ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 29 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 30 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 31 | `const switchId = ref(""), backups = ref([]), selectedBackup = ref(null);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `const loadBackups = async () => { if (!switchId.value) return; backups.value = (await api.get(\`/backups/switches/${switchId.value}\`)).d...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 33 | `const runBackup = async () => { if (!switchId.value) return; await api.post(\`/backups/switches/${switchId.value}/run?backup_type=running...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 34 | `const viewBackup = async (backupId) => { selectedBackup.value = (await api.get(\`/backups/${backupId}\`)).data; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 35 | `</script>` | Fin del bloque de lógica del componente Vue. |