<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { ElButton, ElCard, ElDialog, ElForm, ElFormItem, ElInput, ElInputNumber, ElMessage, ElPopconfirm, ElSelect, ElOption, ElTable, ElTableColumn, ElTag } from 'element-plus'
import { listSwitches, createSwitch, updateSwitch, deleteSwitch, testSsh } from '@/api/network/switches'
import { runDiscovery } from '@/api/network/discovery'
import { runBackup } from '@/api/network/backups'
import SshTerminal from '../components/SshTerminal.vue'

const rows = ref<any[]>([])
const dialog = ref(false)
const terminalDialog = ref(false)
const terminalSwitchId = ref<number | null>(null)
const editingId = ref<number | null>(null)
const form = reactive<any>({ name: '', hostname: '', ip_address: '', brand: '', model: '', os_version: '', ssh_port: 22, ssh_username: '', ssh_password: '', ssh_auth_type: 'password', location: '', rack: '', notes: '' })
const resetForm = () => Object.assign(form, { name: '', hostname: '', ip_address: '', brand: '', model: '', os_version: '', ssh_port: 22, ssh_username: '', ssh_password: '', ssh_auth_type: 'password', location: '', rack: '', notes: '' })
const load = async () => { rows.value = await listSwitches() }
const openCreate = () => { editingId.value = null; resetForm(); dialog.value = true }
const openEdit = (row: any) => { editingId.value = row.id; Object.assign(form, row, { ssh_password: '' }); dialog.value = true }
const save = async () => { editingId.value ? await updateSwitch(editingId.value, form) : await createSwitch(form); dialog.value = false; ElMessage.success('Guardado correctamente'); await load() }
const remove = async (id: number) => { await deleteSwitch(id); ElMessage.success('Switch eliminado'); await load() }
const test = async (id: number) => { const r = await testSsh(id); ElMessage.success(`Estado SSH: ${r.status}`); await load() }
const discover = async (id: number) => { const r = await runDiscovery(id); ElMessage.success(r.summary); await load() }
const backup = async (id: number) => { const r = await runBackup(id); ElMessage.success(`Backup generado: ${r.filename}`) }
const openTerminal = (id: number) => { terminalSwitchId.value = id; terminalDialog.value = true }
onMounted(load)
</script>
<template>
  <div class="p-20px">
    <ElCard>
      <template #header><div class="flex justify-between"><span>Gestión de Switches</span><ElButton type="primary" @click="openCreate">Nuevo switch</ElButton></div></template>
      <ElTable :data="rows" border stripe>
        <ElTableColumn prop="id" label="ID" width="70" />
        <ElTableColumn prop="name" label="Nombre" />
        <ElTableColumn prop="ip_address" label="IP" />
        <ElTableColumn prop="brand" label="Marca" />
        <ElTableColumn prop="model" label="Modelo" />
        <ElTableColumn prop="location" label="Ubicación" />
        <ElTableColumn label="Estado" width="110"><template #default="{ row }"><ElTag :type="row.status === 'online' ? 'success' : row.status === 'offline' ? 'danger' : 'info'">{{ row.status }}</ElTag></template></ElTableColumn>
        <ElTableColumn label="Acciones" width="520"><template #default="{ row }">
          <ElButton size="small" @click="openEdit(row)">Editar</ElButton>
          <ElButton size="small" type="success" @click="test(row.id)">SSH</ElButton>
          <ElButton size="small" type="success" @click="discover(row.id)">Discovery</ElButton>
          <ElButton size="small" type="warning" @click="backup(row.id)">Backup</ElButton>
          <ElButton size="small" @click="openTerminal(row.id)">Consola</ElButton>
          <ElPopconfirm title="¿Eliminar switch?" @confirm="remove(row.id)"><template #reference><ElButton size="small" type="danger">Eliminar</ElButton></template></ElPopconfirm>
        </template></ElTableColumn>
      </ElTable>
    </ElCard>
    <ElDialog v-model="dialog" :title="editingId ? 'Editar switch' : 'Nuevo switch'" width="760px">
      <ElForm label-width="130px">
        <ElFormItem label="Nombre"><ElInput v-model="form.name" /></ElFormItem>
        <ElFormItem label="Hostname"><ElInput v-model="form.hostname" /></ElFormItem>
        <ElFormItem label="IP"><ElInput v-model="form.ip_address" /></ElFormItem>
        <ElFormItem label="Marca"><ElInput v-model="form.brand" placeholder="Cisco / Aruba / HP" /></ElFormItem>
        <ElFormItem label="Modelo"><ElInput v-model="form.model" /></ElFormItem>
        <ElFormItem label="Versión OS"><ElInput v-model="form.os_version" /></ElFormItem>
        <ElFormItem label="Puerto SSH"><ElInputNumber v-model="form.ssh_port" :min="1" :max="65535" /></ElFormItem>
        <ElFormItem label="Usuario SSH"><ElInput v-model="form.ssh_username" /></ElFormItem>
        <ElFormItem label="Contraseña SSH"><ElInput v-model="form.ssh_password" type="password" show-password /></ElFormItem>
        <ElFormItem label="Auth"><ElSelect v-model="form.ssh_auth_type"><ElOption label="password" value="password" /><ElOption label="key" value="key" /></ElSelect></ElFormItem>
        <ElFormItem label="Ubicación"><ElInput v-model="form.location" /></ElFormItem>
        <ElFormItem label="Rack"><ElInput v-model="form.rack" /></ElFormItem>
        <ElFormItem label="Notas"><ElInput v-model="form.notes" type="textarea" /></ElFormItem>
      </ElForm>
      <template #footer><ElButton @click="dialog=false">Cancelar</ElButton><ElButton type="primary" @click="save">Guardar</ElButton></template>
    </ElDialog>
    <ElDialog v-model="terminalDialog" title="Consola SSH" width="90%" destroy-on-close>
      <SshTerminal v-if="terminalSwitchId" :switch-id="terminalSwitchId" />
    </ElDialog>
  </div>
</template>
