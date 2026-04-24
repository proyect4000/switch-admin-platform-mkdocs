# frontend/src/views/NeighborsView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/NeighborsView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Vecinos detectados</div>
      <div class="card" style="margin-bottom:16px;">
        <div class="toolbar">
          <input v-model="switchId" placeholder="Ingrese ID del switch" style="max-width:220px;" />
          <button @click="loadNeighbors">Consultar</button>
        </div>
      </div>
      <div class="card table-wrapper">
        <table>
          <thead><tr><th>ID</th><th>Puerto local</th><th>Vecino</th><th>IP vecina</th><th>Plataforma</th><th>Puerto remoto</th><th>Protocolo</th></tr></thead>
          <tbody><tr v-for="item in neighbors" :key="item.id"><td>{{ item.id }}</td><td>{{ item.local_port }}</td><td>{{ item.neighbor_name }}</td><td>{{ item.neighbor_ip }}</td><td>{{ item.neighbor_platform }}</td><td>{{ item.neighbor_port }}</td><td>{{ item.protocol }}</td></tr></tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "../api/client";
import AppSidebar from "../components/AppSidebar.vue";
const switchId = ref(""), neighbors = ref([]);
const loadNeighbors = async () => { if (!switchId.value) return; neighbors.value = (await api.get(`/discovery/switches/${switchId.value}/neighbors`)).data; };
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Vecinos detectados</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="card" style="margin-bottom:16px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <div class="toolbar">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `          <input v-model="switchId" placeholder="Ingrese ID del switch" style="max-width:220px;" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `          <button @click="loadNeighbors">Consultar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 11 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 12 | `      <div class="card table-wrapper">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `        <table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 14 | `          <thead><tr><th>ID</th><th>Puerto local</th><th>Vecino</th><th>IP vecina</th><th>Plataforma</th><th>Puerto remoto</th><th>Protoc...` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 15 | `          <tbody><tr v-for="item in neighbors" :key="item.id"><td>{{ item.id }}</td><td>{{ item.local_port }}</td><td>{{ item.neighbor_na...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `        </table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 17 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 18 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 19 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 20 | `</template>` | Fin del bloque de plantilla de Vue. |
| 21 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 22 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 23 | `import { ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 24 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 25 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 26 | `const switchId = ref(""), neighbors = ref([]);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `const loadNeighbors = async () => { if (!switchId.value) return; neighbors.value = (await api.get(\`/discovery/switches/${switchId.value}...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `</script>` | Fin del bloque de lógica del componente Vue. |