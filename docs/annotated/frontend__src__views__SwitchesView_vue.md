# frontend/src/views/SwitchesView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/SwitchesView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Gestión de switches</div>
      <div class="toolbar">
        <button @click="openCreate">Nuevo switch</button>
        <button class="secondary" @click="loadSwitches">Recargar</button>
      </div>
      <div class="card table-wrapper">
        <table>
          <thead><tr><th>ID</th><th>Nombre</th><th>IP</th><th>Marca</th><th>Modelo</th><th>Ubicación</th><th>Estado</th><th style="width:420px;">Acciones</th></tr></thead>
          <tbody>
            <tr v-for="item in switches" :key="item.id">
              <td>{{ item.id }}</td><td>{{ item.name }}</td><td>{{ item.ip_address }}</td><td>{{ item.brand }}</td><td>{{ item.model }}</td><td>{{ item.location }}</td>
              <td><span class="badge" :class="item.status || 'unknown'">{{ item.status || "unknown" }}</span></td>
              <td><div style="display:flex; gap:8px; flex-wrap:wrap;">
                <button @click="editSwitch(item)">Editar</button>
                <button class="success" @click="testSSH(item.id)">Probar SSH</button>
                <button class="success" @click="runDiscovery(item.id)">Descubrir</button>
                <button class="secondary" @click="runBackup(item.id)">Backup</button>
                <button class="secondary" @click="openTerminal(item.id)">Consola</button>
                <button class="danger" @click="deleteSwitch(item.id)">Eliminar</button>
              </div></td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
    <SwitchFormModal v-if="showForm" :current="selectedSwitch" @close="closeForm" @saved="loadSwitches" />
    <SshTerminalModal v-if="showTerminal" :switchId="terminalSwitchId" @close="showTerminal = false" />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../api/client";
import AppSidebar from "../components/AppSidebar.vue";
import SwitchFormModal from "../components/SwitchFormModal.vue";
import SshTerminalModal from "../components/SshTerminalModal.vue";
const switches = ref([]), showForm = ref(false), selectedSwitch = ref(null), showTerminal = ref(false), terminalSwitchId = ref(null);
const loadSwitches = async () => { const { data } = await api.get("/switches"); switches.value = data; };
const openCreate = () => { selectedSwitch.value = null; showForm.value = true; };
const editSwitch = (item) => { selectedSwitch.value = item; showForm.value = true; };
const closeForm = () => { showForm.value = false; selectedSwitch.value = null; };
const deleteSwitch = async (id) => { if (!confirm("¿Desea eliminar este switch?")) return; await api.delete(`/switches/${id}`); await loadSwitches(); };
const testSSH = async (id) => { await api.post(`/switches/${id}/test-ssh`); await loadSwitches(); };
const runDiscovery = async (id) => { const { data } = await api.post(`/discovery/switches/${id}/run`); alert(data.summary); await loadSwitches(); };
const runBackup = async (id) => { const { data } = await api.post(`/backups/switches/${id}/run?backup_type=running-config`); alert(`Backup generado: ${data.filename}`); };
const openTerminal = (id) => { terminalSwitchId.value = id; showTerminal.value = true; };
onMounted(loadSwitches);
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Gestión de switches</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="toolbar">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <button @click="openCreate">Nuevo switch</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `        <button class="secondary" @click="loadSwitches">Recargar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 10 | `      <div class="card table-wrapper">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        <table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 12 | `          <thead><tr><th>ID</th><th>Nombre</th><th>IP</th><th>Marca</th><th>Modelo</th><th>Ubicación</th><th>Estado</th><th style="width:...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `          <tbody>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 14 | `            <tr v-for="item in switches" :key="item.id">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `              <td>{{ item.id }}</td><td>{{ item.name }}</td><td>{{ item.ip_address }}</td><td>{{ item.brand }}</td><td>{{ item.model }}</...` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 16 | `              <td><span class="badge" :class="item.status \|\| 'unknown'">{{ item.status \|\| "unknown" }}</span></td>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `              <td><div style="display:flex; gap:8px; flex-wrap:wrap;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `                <button @click="editSwitch(item)">Editar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `                <button class="success" @click="testSSH(item.id)">Probar SSH</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `                <button class="success" @click="runDiscovery(item.id)">Descubrir</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `                <button class="secondary" @click="runBackup(item.id)">Backup</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `                <button class="secondary" @click="openTerminal(item.id)">Consola</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `                <button class="danger" @click="deleteSwitch(item.id)">Eliminar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `              </div></td>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 25 | `            </tr>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 26 | `          </tbody>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 27 | `        </table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 28 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 29 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 30 | `    <SwitchFormModal v-if="showForm" :current="selectedSwitch" @close="closeForm" @saved="loadSwitches" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `    <SshTerminalModal v-if="showTerminal" :switchId="terminalSwitchId" @close="showTerminal = false" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 33 | `</template>` | Fin del bloque de plantilla de Vue. |
| 34 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 35 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 36 | `import { onMounted, ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 37 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 38 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 39 | `import SwitchFormModal from "../components/SwitchFormModal.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 40 | `import SshTerminalModal from "../components/SshTerminalModal.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 41 | `const switches = ref([]), showForm = ref(false), selectedSwitch = ref(null), showTerminal = ref(false), terminalSwitchId = ref(null);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 42 | `const loadSwitches = async () => { const { data } = await api.get("/switches"); switches.value = data; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 43 | `const openCreate = () => { selectedSwitch.value = null; showForm.value = true; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `const editSwitch = (item) => { selectedSwitch.value = item; showForm.value = true; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 45 | `const closeForm = () => { showForm.value = false; selectedSwitch.value = null; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 46 | `const deleteSwitch = async (id) => { if (!confirm("¿Desea eliminar este switch?")) return; await api.delete(\`/switches/${id}\`); await l...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 47 | `const testSSH = async (id) => { await api.post(\`/switches/${id}/test-ssh\`); await loadSwitches(); };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 48 | `const runDiscovery = async (id) => { const { data } = await api.post(\`/discovery/switches/${id}/run\`); alert(data.summary); await loadS...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 49 | `const runBackup = async (id) => { const { data } = await api.post(\`/backups/switches/${id}/run?backup_type=running-config\`); alert(\`Ba...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 50 | `const openTerminal = (id) => { terminalSwitchId.value = id; showTerminal.value = true; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 51 | `onMounted(loadSwitches);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 52 | `</script>` | Fin del bloque de lógica del componente Vue. |