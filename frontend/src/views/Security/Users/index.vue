<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { ElButton, ElCard, ElDialog, ElForm, ElFormItem, ElInput, ElMessage, ElOption, ElPopconfirm, ElSelect, ElSwitch, ElTable, ElTableColumn, ElTag } from 'element-plus'
import { listUsers, createUser, updateUser, disableUser, listRoles } from '@/api/network/users'
const rows = ref<any[]>([])
const roles = ref<any[]>([])
const dialog = ref(false)
const editingId = ref<number | null>(null)
const form = reactive<any>({ username: '', full_name: '', email: '', password: '', role: 'viewer', is_active: true })
const load = async () => { rows.value = await listUsers(); roles.value = await listRoles() }
const reset = () => Object.assign(form, { username: '', full_name: '', email: '', password: '', role: 'viewer', is_active: true })
const openCreate = () => { editingId.value = null; reset(); dialog.value = true }
const openEdit = (row: any) => { editingId.value = row.id; Object.assign(form, row, { password: '' }); dialog.value = true }
const save = async () => { editingId.value ? await updateUser(editingId.value, form) : await createUser(form); dialog.value = false; ElMessage.success('Usuario guardado'); await load() }
const disable = async (id: number) => { await disableUser(id); ElMessage.success('Usuario desactivado'); await load() }
onMounted(load)
</script>
<template><div class="p-20px"><ElCard><template #header><div class="flex justify-between"><span>Usuarios del Sistema</span><ElButton type="primary" @click="openCreate">Nuevo usuario</ElButton></div></template><ElTable :data="rows" border><ElTableColumn prop="id" label="ID" width="70"/><ElTableColumn prop="username" label="Usuario"/><ElTableColumn prop="full_name" label="Nombre"/><ElTableColumn prop="email" label="Correo"/><ElTableColumn label="Rol"><template #default="{row}"><ElTag>{{ row.role }}</ElTag></template></ElTableColumn><ElTableColumn label="Activo"><template #default="{row}"><ElTag :type="row.is_active ? 'success' : 'danger'">{{ row.is_active ? 'Sí' : 'No' }}</ElTag></template></ElTableColumn><ElTableColumn label="Acciones" width="220"><template #default="{row}"><ElButton size="small" @click="openEdit(row)">Editar</ElButton><ElPopconfirm title="¿Desactivar usuario?" @confirm="disable(row.id)"><template #reference><ElButton size="small" type="danger">Desactivar</ElButton></template></ElPopconfirm></template></ElTableColumn></ElTable></ElCard><ElDialog v-model="dialog" :title="editingId ? 'Editar usuario' : 'Nuevo usuario'" width="640px"><ElForm label-width="120px"><ElFormItem label="Usuario"><ElInput v-model="form.username"/></ElFormItem><ElFormItem label="Nombre"><ElInput v-model="form.full_name"/></ElFormItem><ElFormItem label="Correo"><ElInput v-model="form.email"/></ElFormItem><ElFormItem label="Contraseña"><ElInput v-model="form.password" type="password" show-password/></ElFormItem><ElFormItem label="Rol"><ElSelect v-model="form.role"><ElOption v-for="r in roles" :key="r.name" :label="r.label" :value="r.name"/></ElSelect></ElFormItem><ElFormItem label="Activo"><ElSwitch v-model="form.is_active"/></ElFormItem></ElForm><template #footer><ElButton @click="dialog=false">Cancelar</ElButton><ElButton type="primary" @click="save">Guardar</ElButton></template></ElDialog></div></template>
