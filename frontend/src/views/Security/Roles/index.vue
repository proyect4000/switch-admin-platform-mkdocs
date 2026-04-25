<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { ElCard, ElTable, ElTableColumn, ElTag } from 'element-plus'
import { listRoles } from '@/api/network/users'
const roles = ref<any[]>([])
onMounted(async () => roles.value = await listRoles())
</script>
<template><div class="p-20px"><ElCard><template #header>Roles y Permisos</template><ElTable :data="roles" border><ElTableColumn prop="name" label="Rol" width="160"/><ElTableColumn prop="label" label="Descripción" width="240"/><ElTableColumn label="Permisos"><template #default="{row}"><ElTag v-for="p in row.permissions" :key="p" class="mr-6px mb-6px" type="info">{{ p }}</ElTag></template></ElTableColumn></ElTable></ElCard></div></template>
