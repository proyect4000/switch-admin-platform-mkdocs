# frontend/src/views/JobsView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/JobsView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Tareas programadas</div>
      <div class="card" style="margin-bottom:16px;">
        <div class="form-grid">
          <div><label>Nombre</label><input v-model="form.job_name" placeholder="Ej. Discovery Core Switch" /></div>
          <div><label>Tipo</label><select v-model="form.job_type"><option value="discovery">discovery</option><option value="backup">backup</option></select></div>
          <div><label>Cron</label><input v-model="form.cron_expression" placeholder="*/30 * * * *" /></div>
          <div><label>ID switch</label><input v-model.number="form.target_switch_id" type="number" /></div>
        </div>
        <div class="form-actions"><button @click="createJob">Guardar tarea</button></div>
      </div>
      <div class="card table-wrapper">
        <table>
          <thead><tr><th>ID</th><th>Nombre</th><th>Tipo</th><th>Cron</th><th>Switch</th><th>Activo</th><th>Fecha creación</th><th>Acción</th></tr></thead>
          <tbody><tr v-for="item in jobs" :key="item.id"><td>{{ item.id }}</td><td>{{ item.job_name }}</td><td>{{ item.job_type }}</td><td>{{ item.cron_expression }}</td><td>{{ item.target_switch_id }}</td><td>{{ item.is_active ? "Sí" : "No" }}</td><td>{{ item.created_at }}</td><td><button class="secondary" @click="toggleJob(item.id)">Activar / Desactivar</button></td></tr></tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import api from "../api/client";
import AppSidebar from "../components/AppSidebar.vue";
const jobs = ref([]);
const form = reactive({ job_name:"", job_type:"discovery", cron_expression:"*/30 * * * *", target_switch_id:null, is_active:true });
const loadJobs = async () => { jobs.value = (await api.get("/jobs")).data; };
const createJob = async () => { await api.post("/jobs", form); Object.assign(form, { job_name:"", job_type:"discovery", cron_expression:"*/30 * * * *", target_switch_id:null, is_active:true }); await loadJobs(); };
const toggleJob = async (id) => { await api.put(`/jobs/${id}/toggle`); await loadJobs(); };
onMounted(loadJobs);
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Tareas programadas</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="card" style="margin-bottom:16px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <div class="form-grid">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `          <div><label>Nombre</label><input v-model="form.job_name" placeholder="Ej. Discovery Core Switch" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `          <div><label>Tipo</label><select v-model="form.job_type"><option value="discovery">discovery</option><option value="backup">back...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `          <div><label>Cron</label><input v-model="form.cron_expression" placeholder="*/30 * * * *" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `          <div><label>ID switch</label><input v-model.number="form.target_switch_id" type="number" /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 13 | `        <div class="form-actions"><button @click="createJob">Guardar tarea</button></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 14 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 15 | `      <div class="card table-wrapper">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `        <table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 17 | `          <thead><tr><th>ID</th><th>Nombre</th><th>Tipo</th><th>Cron</th><th>Switch</th><th>Activo</th><th>Fecha creación</th><th>Acción<...` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 18 | `          <tbody><tr v-for="item in jobs" :key="item.id"><td>{{ item.id }}</td><td>{{ item.job_name }}</td><td>{{ item.job_type }}</td><t...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 19 | `        </table>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 20 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 21 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 22 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 23 | `</template>` | Fin del bloque de plantilla de Vue. |
| 24 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 25 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 26 | `import { onMounted, reactive, ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 27 | `import api from "../api/client";` | Importa un módulo o paquete necesario para este archivo. |
| 28 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 29 | `const jobs = ref([]);` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `const form = reactive({ job_name:"", job_type:"discovery", cron_expression:"*/30 * * * *", target_switch_id:null, is_active:true });` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `const loadJobs = async () => { jobs.value = (await api.get("/jobs")).data; };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `const createJob = async () => { await api.post("/jobs", form); Object.assign(form, { job_name:"", job_type:"discovery", cron_expression:"...` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 33 | `const toggleJob = async (id) => { await api.put(\`/jobs/${id}/toggle\`); await loadJobs(); };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 34 | `onMounted(loadJobs);` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 35 | `</script>` | Fin del bloque de lógica del componente Vue. |