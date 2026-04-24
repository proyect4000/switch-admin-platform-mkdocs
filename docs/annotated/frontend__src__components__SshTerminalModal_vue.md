# frontend/src/components/SshTerminalModal.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/components/SshTerminalModal.vue`.

## Código fuente

```vue
<template>
  <div class="modal-backdrop">
    <div class="modal large" style="background:#111827; color:white;">
      <div class="modal-header">
        <h3>Consola SSH</h3>
        <button class="secondary" @click="closeTerminal">Cerrar</button>
      </div>
      <div id="terminal" style="height:600px; width:100%;"></div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from "vue";
import { Terminal } from "@xterm/xterm";
import "@xterm/xterm/css/xterm.css";
const props = defineProps({ switchId: { type: Number, required: true } });
const emit = defineEmits(["close"]);
let socket = null;
let term = null;
const closeTerminal = () => { if (socket) socket.close(); emit("close"); };
onMounted(() => {
  const token = localStorage.getItem("token");
  const wsBase = import.meta.env.VITE_WS_URL || "ws://localhost:8000";
  term = new Terminal({ cursorBlink: true, cols: 120, rows: 30 });
  term.open(document.getElementById("terminal"));
  term.write("Iniciando sesión SSH...\r\n");
  socket = new WebSocket(`${wsBase}/ws/ssh/${props.switchId}?token=${encodeURIComponent(token)}`);
  socket.onopen = () => term.write("Conexión establecida\r\n");
  socket.onmessage = (event) => term.write(event.data);
  socket.onerror = () => term.write("\r\n[ERROR] Falló la conexión WebSocket\r\n");
  socket.onclose = () => term.write("\r\nConexión finalizada\r\n");
  term.onData((data) => {
    if (socket && socket.readyState === WebSocket.OPEN) socket.send(data);
  });
});
onBeforeUnmount(() => { if (socket) socket.close(); if (term) term.dispose(); });
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="modal-backdrop">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <div class="modal large" style="background:#111827; color:white;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 4 | `      <div class="modal-header">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `        <h3>Consola SSH</h3>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 6 | `        <button class="secondary" @click="closeTerminal">Cerrar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 8 | `      <div id="terminal" style="height:600px; width:100%;"></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `    </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 10 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 11 | `</template>` | Fin del bloque de plantilla de Vue. |
| 12 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 13 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 14 | `import { onMounted, onBeforeUnmount } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 15 | `import { Terminal } from "@xterm/xterm";` | Importa un módulo o paquete necesario para este archivo. |
| 16 | `import "@xterm/xterm/css/xterm.css";` | Importa un módulo o paquete necesario para este archivo. |
| 17 | `const props = defineProps({ switchId: { type: Number, required: true } });` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `const emit = defineEmits(["close"]);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `let socket = null;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `let term = null;` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `const closeTerminal = () => { if (socket) socket.close(); emit("close"); };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `onMounted(() => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `  const token = localStorage.getItem("token");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 24 | `  const wsBase = import.meta.env.VITE_WS_URL \|\| "ws://localhost:8000";` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `  term = new Terminal({ cursorBlink: true, cols: 120, rows: 30 });` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `  term.open(document.getElementById("terminal"));` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 27 | `  term.write("Iniciando sesión SSH...\r\n");` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 28 | `  socket = new WebSocket(\`${wsBase}/ws/ssh/${props.switchId}?token=${encodeURIComponent(token)}\`);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `  socket.onopen = () => term.write("Conexión establecida\r\n");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `  socket.onmessage = (event) => term.write(event.data);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `  socket.onerror = () => term.write("\r\n[ERROR] Falló la conexión WebSocket\r\n");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `  socket.onclose = () => term.write("\r\nConexión finalizada\r\n");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 33 | `  term.onData((data) => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 34 | `    if (socket && socket.readyState === WebSocket.OPEN) socket.send(data);` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 35 | `  });` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 36 | `});` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 37 | `onBeforeUnmount(() => { if (socket) socket.close(); if (term) term.dispose(); });` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 38 | `</script>` | Fin del bloque de lógica del componente Vue. |