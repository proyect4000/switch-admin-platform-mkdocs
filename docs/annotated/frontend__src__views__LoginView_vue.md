# frontend/src/views/LoginView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/LoginView.vue`.

## Código fuente

```vue
<template>
  <div class="login-page">
    <div class="login-card">
      <div style="text-align:center; margin-bottom:20px; font-size:24px;">Iniciar sesión</div>
      <form @submit.prevent="handleLogin">
        <div style="margin-bottom: 12px;">
          <label>Usuario</label>
          <input v-model="username" placeholder="Ingrese su usuario" />
        </div>
        <div style="margin-bottom: 12px;">
          <label>Contraseña</label>
          <input v-model="password" type="password" placeholder="Ingrese su contraseña" />
        </div>
        <button type="submit" style="width:100%;">Ingresar</button>
      </form>
      <div v-if="error" style="color:#dc2626; margin-top:10px;">{{ error }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
const auth = useAuthStore();
const router = useRouter();
const username = ref("");
const password = ref("");
const error = ref("");
const handleLogin = async () => {
  error.value = "";
  try {
    await auth.login(username.value, password.value);
    await auth.fetchMe();
    router.push("/dashboard");
  } catch {
    error.value = "Usuario o contraseña incorrectos";
  }
};
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="login-page">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <div class="login-card">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 4 | `      <div style="text-align:center; margin-bottom:20px; font-size:24px;">Iniciar sesión</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <form @submit.prevent="handleLogin">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `        <div style="margin-bottom: 12px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `          <label>Usuario</label>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 8 | `          <input v-model="username" placeholder="Ingrese su usuario" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 9 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 10 | `        <div style="margin-bottom: 12px;">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 11 | `          <label>Contraseña</label>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 12 | `          <input v-model="password" type="password" placeholder="Ingrese su contraseña" />` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 13 | `        </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 14 | `        <button type="submit" style="width:100%;">Ingresar</button>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 15 | `      </form>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 16 | `      <div v-if="error" style="color:#dc2626; margin-top:10px;">{{ error }}</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 17 | `    </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 18 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 19 | `</template>` | Fin del bloque de plantilla de Vue. |
| 20 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 21 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 22 | `import { ref } from "vue";` | Importa un módulo o paquete necesario para este archivo. |
| 23 | `import { useRouter } from "vue-router";` | Importa un módulo o paquete necesario para este archivo. |
| 24 | `import { useAuthStore } from "../stores/auth";` | Importa un módulo o paquete necesario para este archivo. |
| 25 | `const auth = useAuthStore();` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 26 | `const router = useRouter();` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 27 | `const username = ref("");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 28 | `const password = ref("");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 29 | `const error = ref("");` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 30 | `const handleLogin = async () => {` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 31 | `  error.value = "";` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 32 | `  try {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 33 | `    await auth.login(username.value, password.value);` | Espera el resultado de una operación asíncrona antes de continuar. |
| 34 | `    await auth.fetchMe();` | Espera el resultado de una operación asíncrona antes de continuar. |
| 35 | `    router.push("/dashboard");` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 36 | `  } catch {` | Abre un bloque de configuración, estilos o estructura de objeto. |
| 37 | `    error.value = "Usuario o contraseña incorrectos";` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 38 | `  }` | Símbolo de estructura que abre o cierra un bloque o agrupación. |
| 39 | `};` | Instrucción de JavaScript/CSS terminada explícitamente. |
| 40 | `</script>` | Fin del bloque de lógica del componente Vue. |