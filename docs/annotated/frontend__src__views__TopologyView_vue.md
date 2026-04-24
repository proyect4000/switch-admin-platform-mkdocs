# frontend/src/views/TopologyView.vue

## Propósito

Archivo del proyecto ubicado en `frontend/src/views/TopologyView.vue`.

## Código fuente

```vue
<template>
  <div class="page-layout">
    <AppSidebar />
    <main class="page-content">
      <div class="page-title">Mapa de Topología</div>
      <div class="card"><TopologyMap /></div>
    </main>
  </div>
</template>

<script setup>
import AppSidebar from "../components/AppSidebar.vue";
import TopologyMap from "../components/TopologyMap.vue";
</script>
```

## Explicación línea por línea

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `<template>` | Inicio del bloque de plantilla de Vue, donde se define la interfaz visual. |
| 2 | `  <div class="page-layout">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 3 | `    <AppSidebar />` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 4 | `    <main class="page-content">` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 5 | `      <div class="page-title">Mapa de Topología</div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 6 | `      <div class="card"><TopologyMap /></div>` | Asigna un valor a una variable o atributo para usarlo más adelante. |
| 7 | `    </main>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 8 | `  </div>` | Elemento de interfaz o estructura HTML/Vue utilizado para construir la vista. |
| 9 | `</template>` | Fin del bloque de plantilla de Vue. |
| 10 | `` | Línea en blanco para separar bloques y mejorar la legibilidad. |
| 11 | `<script setup>` | Inicio del bloque de lógica JavaScript del componente Vue. |
| 12 | `import AppSidebar from "../components/AppSidebar.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 13 | `import TopologyMap from "../components/TopologyMap.vue";` | Importa un módulo o paquete necesario para este archivo. |
| 14 | `</script>` | Fin del bloque de lógica del componente Vue. |