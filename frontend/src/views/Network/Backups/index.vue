<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElCard, ElDialog, ElInputNumber, ElMessage, ElTable, ElTableColumn } from 'element-plus'
import { listBackups, runBackup, getBackup } from '@/api/network/backups'
const switchId = ref<number>()
const rows = ref<any[]>([])
const content = ref('')
const dialog = ref(false)
const load = async () => { if (switchId.value) rows.value = await listBackups(switchId.value) }
const backup = async () => { if (!switchId.value) return; const r = await runBackup(switchId.value); ElMessage.success(`Backup generado: ${r.filename}`); await load() }
const view = async (id: number) => { const r = await getBackup(id); content.value = r.content; dialog.value = true }
</script>
<template><div class="p-20px"><ElCard><template #header>Backups de configuración</template><div class="mb-16px flex gap-8px"><ElInputNumber v-model="switchId" placeholder="ID switch"/><ElButton @click="load">Consultar</ElButton><ElButton type="success" @click="backup">Generar backup</ElButton></div><ElTable :data="rows" border><ElTableColumn prop="id" label="ID" width="70"/><ElTableColumn prop="switch_id" label="Switch"/><ElTableColumn prop="backup_type" label="Tipo"/><ElTableColumn prop="filename" label="Archivo"/><ElTableColumn prop="created_at" label="Fecha"/><ElTableColumn label="Acción"><template #default="{row}"><ElButton size="small" @click="view(row.id)">Ver</ElButton></template></ElTableColumn></ElTable></ElCard><ElDialog v-model="dialog" title="Contenido del backup" width="80%"><pre style="background:#0f172a;color:#e2e8f0;padding:16px;border-radius:8px;max-height:520px;overflow:auto;white-space:pre-wrap">{{ content }}</pre></ElDialog></div></template>
