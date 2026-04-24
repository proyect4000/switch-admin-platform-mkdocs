# frontend/src/components/SwitchFormModal.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/components/SwitchFormModal.vue`.

## Código fuente

```vue
<template>
  <div class="modal-backdrop">
    <div class="modal">
      <div class="modal-header">
        <h3>{{ form.id ? "Editar switch" : "Nuevo switch" }}</h3>
        <button class="secondary" @click="$emit('close')">Cerrar</button>
      </div>
      <form @submit.prevent="submitForm">
        <div class="form-grid">
          <div><label>Nombre</label><input v-model="form.name" required /></div>
          <div><label>Hostname</label><input v-model="form.hostname" /></div>
          <div><label>IP</label><input v-model="form.ip_address" required /></div>
          <div><label>Marca</label><input v-model="form.brand" /></div>
          <div><label>Modelo</label><input v-model="form.model" /></div>
          <div><label>Versión OS</label><input v-model="form.os_version" /></div>
          <div><label>Puerto SSH</label><input v-model.number="form.ssh_port" type="number" /></div>
          <div><label>Usuario SSH</label><input v-model="form.ssh_username" required /></div>
          <div><label>Contraseña SSH</label><input v-model="form.ssh_password" type="password" /></div>
          <div><label>Tipo auth</label><select v-model="form.ssh_auth_type"><option value="password">password</option><option value="key">key</option></select></div>
          <div><label>Ubicación</label><input v-model="form.location" /></div>
          <div><label>Rack</label><input v-model="form.rack" /></div>
          <div style="grid-column:1 / -1;"><label>Notas</label><textarea v-model="form.notes"></textarea></div>
        </div>
        <div class="form-actions">
          <button type="button" class="secondary" @click="$emit('close')">Cancelar</button>
          <button type="submit">{{ form.id ? "Actualizar" : "Guardar" }}</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from "vue";
import api from "../api/client";
const props = defineProps({ current: { type: Object, default: null } });
const emit = defineEmits(["close", "saved"]);
const form = reactive({ id:null, name:"", hostname:"", ip_address:"", brand:"", model:"", os_version:"", ssh_port:22, ssh_username:"", ssh_password:"", ssh_auth_type:"password", location:"", rack:"", notes:"" });
watch(() => props.current, (value) => {
  if (value) Object.assign(form, { ...value, ssh_password: "" });
  else Object.assign(form, { id:null, name:"", hostname:"", ip_address:"", brand:"", model:"", os_version:"", ssh_port:22, ssh_username:"", ssh_password:"", ssh_auth_type:"password", location:"", rack:"", notes:"" });
}, { immediate: true });
const submitForm = async () => {
  const payload = { ...form };
  if (!payload.ssh_password) delete payload.ssh_password;
  if (form.id) await api.put(`/switches/${form.id}`, payload);
  else await api.post("/switches", payload);
  emit("saved"); emit("close");
};
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="modal-backdrop">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <div class="modal">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 4 | `      <div class="modal-header">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `        <h3>{{ form.id ? "Editar switch" : "Nuevo switch" }}</h3>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 6 | `        <button class="secondary" @click="$emit('close')">Cerrar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 8 | `      <form @submit.prevent="submitForm">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `        <div class="form-grid">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `          <div><label>Nombre</label><input v-model="form.name" required /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `          <div><label>Hostname</label><input v-model="form.hostname" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `          <div><label>IP</label><input v-model="form.ip_address" required /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `          <div><label>Marca</label><input v-model="form.brand" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `          <div><label>Modelo</label><input v-model="form.model" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `          <div><label>Versión OS</label><input v-model="form.os_version" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `          <div><label>Puerto SSH</label><input v-model.number="form.ssh_port" type="number" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `          <div><label>Usuario SSH</label><input v-model="form.ssh_username" required /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 18 | `          <div><label>Contraseña SSH</label><input v-model="form.ssh_password" type="password" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `          <div><label>Tipo auth</label><select v-model="form.ssh_auth_type"><option value="password">password</option><option value="key"...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 20 | `          <div><label>Ubicación</label><input v-model="form.location" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `          <div><label>Rack</label><input v-model="form.rack" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 22 | `          <div style="grid-column:1 / -1;"><label>Notas</label><textarea v-model="form.notes"></textarea></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 23 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 24 | `        <div class="form-actions">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 25 | `          <button type="button" class="secondary" @click="$emit('close')">Cancelar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `          <button type="submit">{{ form.id ? "Actualizar" : "Guardar" }}</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 28 | `      </form>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 29 | `    </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 30 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 31 | `</template>` | Fin del bloque de plantilla de Vue. |
| 32 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 33 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 34 | `import { reactive, watch } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 35 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 36 | `const props = defineProps({ current: { type: Object, default: null } });` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 37 | `const emit = defineEmits(["close", "saved"]);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 38 | `const form = reactive({ id:null, name:"", hostname:"", ip_address:"", brand:"", model:"", os_version:"", ssh_port:22, ssh_username:"", ss...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 39 | `watch(() => props.current, (value) => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 40 | `  if (value) Object.assign(form, { ...value, ssh_password: "" });` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 41 | `  else Object.assign(form, { id:null, name:"", hostname:"", ip_address:"", brand:"", model:"", os_version:"", ssh_port:22, ssh_username:"...` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 42 | `}, { immediate: true });` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 43 | `const submitForm = async () => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 44 | `  const payload = { ...form };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 45 | `  if (!payload.ssh_password) delete payload.ssh_password;` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 46 | `  if (form.id) await api.put(\`/switches/${form.id}\`, payload);` | Condición principal que decide si se ejecuta el bloque siguiente. |
| 47 | `  else await api.post("/switches", payload);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 48 | `  emit("saved"); emit("close");` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 49 | `};` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 50 | `</script>` | Fin del bloque de lógica del componente Vue. |