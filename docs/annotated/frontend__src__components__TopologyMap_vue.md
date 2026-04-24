# frontend/src/components/TopologyMap.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/components/TopologyMap.vue`.

## Código fuente

```vue
<template>
  <div class="topology-layout">
    <div id="network"></div>
    <div class="card side-panel" v-if="selectedNode">
      <h3>Switch seleccionado</h3>
      <p><strong>ID:</strong> {{ selectedNode.id }}</p>
      <p><strong>Nombre:</strong> {{ selectedNode.label }}</p>
      <div style="display:flex; flex-direction:column; gap:10px; margin-top:14px;">
        <button @click="openTerminal">Abrir consola SSH</button>
        <button class="secondary" @click="runDiscovery">Ejecutar discovery</button>
        <button class="danger" @click="deleteNode">Eliminar switch</button>
      </div>
    </div>
    <SshTerminalModal v-if="showTerminal" :switchId="selectedNode.id" @close="showTerminal = false" />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { Network } from "vis-network/standalone";
import api from "../api/client";
import SshTerminalModal from "./SshTerminalModal.vue";

const selectedNode = ref(null);
const showTerminal = ref(false);
let network = null;
let latestData = null;

const loadTopology = async () => {
  const { data } = await api.get("/topology");
  latestData = data;
  const container = document.getElementById("network");
  if (network) network.destroy();
  network = new Network(container, data, {
    autoResize: true, physics: { enabled: true }, interaction: { hover: true },
    nodes: { shape: "box", margin: 12, font: { size: 14 } },
    edges: { smooth: true, font: { align: "middle" } },
    groups: {
      online: { color: { background: "#dcfce7", border: "#16a34a" } },
      offline: { color: { background: "#fee2e2", border: "#dc2626" } },
      unknown: { color: { background: "#e5e7eb", border: "#6b7280" } }
    }
  });
  network.on("click", (params) => {
    if (params.nodes.length > 0) {
      const id = params.nodes[0];
      selectedNode.value = latestData.nodes.find(n => n.id === id);
    }
  });
};
const openTerminal = () => { showTerminal.value = true; };
const runDiscovery = async () => {
  if (!selectedNode.value) return;
  const { data } = await api.post(`/discovery/switches/${selectedNode.value.id}/run`);
  alert(data.summary); await loadTopology();
};
const deleteNode = async () => {
  if (!selectedNode.value) return;
  if (!confirm("¿Desea eliminar este switch del sistema?")) return;
  await api.delete(`/switches/${selectedNode.value.id}`);
  selectedNode.value = null; await loadTopology();
};
onMounted(loadTopology);
</script>

<style scoped>
.topology-layout { display: flex; gap: 16px; align-items: flex-start; }
#network { flex: 1; height: 720px; border-radius: 14px; border: 1px solid var(--border); background: white; }
.side-panel { width: 320px; }
</style>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="topology-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <div id="network"></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 4 | `    <div class="card side-panel" v-if="selectedNode">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <h3>Switch seleccionado</h3>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 6 | `      <p><strong>ID:</strong> {{ selectedNode.id }}</p>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 7 | `      <p><strong>Nombre:</strong> {{ selectedNode.label }}</p>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 8 | `      <div style="display:flex; flex-direction:column; gap:10px; margin-top:14px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `        <button @click="openTerminal">Abrir consola SSH</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `        <button class="secondary" @click="runDiscovery">Ejecutar discovery</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        <button class="danger" @click="deleteNode">Eliminar switch</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 13 | `    </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 14 | `    <SshTerminalModal v-if="showTerminal" :switchId="selectedNode.id" @close="showTerminal = false" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 16 | `</template>` | Fin del bloque de plantilla de Vue. |
| 17 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 18 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 19 | `import { onMounted, ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 20 | `import { Network } from "vis-network/standalone";` | Importa un módulo o paquete necesario para este archivo. |
| 21 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 22 | `import SshTerminalModal from "./SshTerminalModal.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 23 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 24 | `const selectedNode = ref(null);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `const showTerminal = ref(false);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `let network = null;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `let latestData = null;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 29 | `const loadTopology = async () => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `  const { data } = await api.get("/topology");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `  latestData = data;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `  const container = document.getElementById("network");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 33 | `  if (network) network.destroy();` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 34 | `  network = new Network(container, data, {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 35 | `    autoResize: true, physics: { enabled: true }, interaction: { hover: true },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 36 | `    nodes: { shape: "box", margin: 12, font: { size: 14 } },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 37 | `    edges: { smooth: true, font: { align: "middle" } },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 38 | `    groups: {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 39 | `      online: { color: { background: "#dcfce7", border: "#16a34a" } },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 40 | `      offline: { color: { background: "#fee2e2", border: "#dc2626" } },` | Define una propiedad dentro de un objeto, configuración o estructura de datos. |
| 41 | `      unknown: { color: { background: "#e5e7eb", border: "#6b7280" } }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 42 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 43 | `  });` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 44 | `  network.on("click", (params) => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 45 | `    if (params.nodes.length > 0) {` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 46 | `      const id = params.nodes[0];` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 47 | `      selectedNode.value = latestData.nodes.find(n => n.id === id);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 48 | `    }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 49 | `  });` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 50 | `};` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 51 | `const openTerminal = () => { showTerminal.value = true; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 52 | `const runDiscovery = async () => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 53 | `  if (!selectedNode.value) return;` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 54 | `  const { data } = await api.post(\`/discovery/switches/${selectedNode.value.id}/run\`);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 55 | `  alert(data.summary); await loadTopology();` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 56 | `};` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 57 | `const deleteNode = async () => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 58 | `  if (!selectedNode.value) return;` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 59 | `  if (!confirm("¿Desea eliminar este switch del sistema?")) return;` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 60 | `  await api.delete(\`/switches/${selectedNode.value.id}\`);` | Espera el resultado de una operación asíncrona antes de continuar. |
| 61 | `  selectedNode.value = null; await loadTopology();` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 62 | `};` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 63 | `onMounted(loadTopology);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 64 | `</script>` | Fin del bloque de lógica del componente Vue. |
| 65 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 66 | `<style scoped>` | Inicio del bloque de estilos del componente. |
| 67 | `.topology-layout { display: flex; gap: 16px; align-items: flex-start; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 68 | `#network { flex: 1; height: 720px; border-radius: 14px; border: 1px solid var(--border); background: white; }` | Comentario que documenta o aclara el bloque de código. |
| 69 | `.side-panel { width: 320px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 70 | `</style>` | Fin del bloque de estilos. |