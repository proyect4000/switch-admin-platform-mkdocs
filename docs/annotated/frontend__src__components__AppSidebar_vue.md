# frontend/src/components/AppSidebar.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/components/AppSidebar.vue`.

## Código fuente

```vue
<template>
  <aside class="sidebar">
    <div>
      <div class="brand">Switch Admin</div>
      <nav class="nav">
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
        <router-link to="/switches" class="nav-link">Switches</router-link>
        <router-link to="/topology" class="nav-link">Topología</router-link>
        <router-link to="/neighbors" class="nav-link">Vecinos</router-link>
        <router-link to="/backups" class="nav-link">Backups</router-link>
        <router-link to="/jobs" class="nav-link">Tareas programadas</router-link>
        <router-link to="/history" class="nav-link">Historial</router-link>
      </nav>
    </div>
    <div class="sidebar-footer">
      <div v-if="auth.user" class="user-box">
        <strong>{{ auth.user.full_name }}</strong>
        <small>{{ auth.user.role }}</small>
      </div>
      <button class="secondary" @click="logout">Cerrar sesión</button>
    </div>
  </aside>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
const auth = useAuthStore();
const router = useRouter();
const logout = () => { auth.logout(); router.push("/login"); };
</script>

<style scoped>
.sidebar { width: 270px; min-height: 100vh; background: var(--sidebar); color: white; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; }
.brand { font-size: 22px; font-weight: bold; margin-bottom: 24px; }
.nav { display: flex; flex-direction: column; gap: 8px; }
.nav-link { padding: 12px 14px; border-radius: 10px; color: white; text-decoration: none; }
.nav-link:hover, .router-link-active { background: var(--sidebar-hover); }
.sidebar-footer { display: flex; flex-direction: column; gap: 12px; }
.user-box small { color: #cbd5e1; }
</style>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <aside class="sidebar">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `      <div class="brand">Switch Admin</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <nav class="nav">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `        <router-link to="/switches" class="nav-link">Switches</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 8 | `        <router-link to="/topology" class="nav-link">Topología</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `        <router-link to="/neighbors" class="nav-link">Vecinos</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 10 | `        <router-link to="/backups" class="nav-link">Backups</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `        <router-link to="/jobs" class="nav-link">Tareas programadas</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 12 | `        <router-link to="/history" class="nav-link">Historial</router-link>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `      </nav>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 14 | `    </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 15 | `    <div class="sidebar-footer">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 16 | `      <div v-if="auth.user" class="user-box">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `        <strong>{{ auth.user.full_name }}</strong>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 18 | `        <small>{{ auth.user.role }}</small>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 19 | `      </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 20 | `      <button class="secondary" @click="logout">Cerrar sesión</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 21 | `    </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 22 | `  </aside>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 23 | `</template>` | Fin del bloque de plantilla de Vue. |
| 24 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 25 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 26 | `import { useRouter } from "vue-router";` | Importa un módulo o paquete necesario para este archivo. |
| 27 | `import { useAuthStore } from "../stores/auth";` | Importa un módulo o paquete necesario para este archivo. |
| 28 | `const auth = useAuthStore();` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `const router = useRouter();` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `const logout = () => { auth.logout(); router.push("/login"); };` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `</script>` | Fin del bloque de lógica del componente Vue. |
| 32 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 33 | `<style scoped>` | Inicio del bloque de estilos del componente. |
| 34 | `.sidebar { width: 270px; min-height: 100vh; background: var(--sidebar); color: white; padding: 20px; display: flex; flex-direction: colum...` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 35 | `.brand { font-size: 22px; font-weight: bold; margin-bottom: 24px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 36 | `.nav { display: flex; flex-direction: column; gap: 8px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 37 | `.nav-link { padding: 12px 14px; border-radius: 10px; color: white; text-decoration: none; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 38 | `.nav-link:hover, .router-link-active { background: var(--sidebar-hover); }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 39 | `.sidebar-footer { display: flex; flex-direction: column; gap: 12px; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 40 | `.user-box small { color: #cbd5e1; }` | Línea de implementación que forma parte del comportamiento interno del archivo. |
| 41 | `</style>` | Fin del bloque de estilos. |