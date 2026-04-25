<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { ElButton, ElCard, ElForm, ElFormItem, ElInput, ElInputNumber, ElOption, ElSelect, ElSwitch, ElTable, ElTableColumn } from 'element-plus'
import { listJobs, createJob, toggleJob } from '@/api/network/jobs'
const rows = ref<any[]>([])
const form = reactive({ job_name: '', job_type: 'discovery', cron_expression: '*/30 * * * *', target_switch_id: undefined as number | undefined, is_active: true })
const load = async () => rows.value = await listJobs()
const save = async () => { await createJob(form); Object.assign(form, { job_name: '', job_type: 'discovery', cron_expression: '*/30 * * * *', target_switch_id: undefined, is_active: true }); await load() }
const toggle = async (id: number) => { await toggleJob(id); await load() }
onMounted(load)
</script>
<template><div class="p-20px"><ElCard class="mb-16px"><template #header>Crear tarea programada</template><ElForm label-width="130px"><ElFormItem label="Nombre"><ElInput v-model="form.job_name" /></ElFormItem><ElFormItem label="Tipo"><ElSelect v-model="form.job_type"><ElOption label="Discovery" value="discovery"/><ElOption label="Backup" value="backup"/></ElSelect></ElFormItem><ElFormItem label="Cron"><ElInput v-model="form.cron_expression" placeholder="*/30 * * * *" /></ElFormItem><ElFormItem label="ID Switch"><ElInputNumber v-model="form.target_switch_id" /></ElFormItem><ElFormItem label="Activo"><ElSwitch v-model="form.is_active" /></ElFormItem><ElFormItem><ElButton type="primary" @click="save">Guardar</ElButton></ElFormItem></ElForm></ElCard><ElCard><template #header>Tareas programadas</template><ElTable :data="rows" border><ElTableColumn prop="id" label="ID" width="70"/><ElTableColumn prop="job_name" label="Nombre"/><ElTableColumn prop="job_type" label="Tipo"/><ElTableColumn prop="cron_expression" label="Cron"/><ElTableColumn prop="target_switch_id" label="Switch"/><ElTableColumn prop="is_active" label="Activo"/><ElTableColumn label="Acción"><template #default="{row}"><ElButton size="small" @click="toggle(row.id)">Activar/Desactivar</ElButton></template></ElTableColumn></ElTable></ElCard></div></template>
