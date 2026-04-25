<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { ElCard, ElTabs, ElTabPane, ElTable, ElTableColumn } from 'element-plus'
import { listSessions, listCommands, listAuditLogs } from '@/api/network/history'
const sessions = ref<any[]>([]), commands = ref<any[]>([]), audits = ref<any[]>([])
const load = async () => { sessions.value = await listSessions(); commands.value = await listCommands(); audits.value = await listAuditLogs() }
onMounted(load)
</script>
<template><div class="p-20px"><ElCard><template #header>Historial y Auditoría</template><ElTabs><ElTabPane label="Sesiones SSH"><ElTable :data="sessions" border><ElTableColumn prop="id" label="ID"/><ElTableColumn prop="user_id" label="Usuario"/><ElTableColumn prop="switch_id" label="Switch"/><ElTableColumn prop="client_ip" label="Cliente"/><ElTableColumn prop="status" label="Estado"/><ElTableColumn prop="started_at" label="Inicio"/></ElTable></ElTabPane><ElTabPane label="Comandos"><ElTable :data="commands" border><ElTableColumn prop="id" label="ID"/><ElTableColumn prop="session_id" label="Sesión"/><ElTableColumn prop="command_text" label="Comando"/><ElTableColumn prop="executed_at" label="Fecha"/></ElTable></ElTabPane><ElTabPane label="Auditoría"><ElTable :data="audits" border><ElTableColumn prop="id" label="ID"/><ElTableColumn prop="user_id" label="Usuario"/><ElTableColumn prop="action" label="Acción"/><ElTableColumn prop="entity_type" label="Entidad"/><ElTableColumn prop="detail" label="Detalle"/><ElTableColumn prop="created_at" label="Fecha"/></ElTable></ElTabPane></ElTabs></ElCard></div></template>
