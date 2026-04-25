<script setup lang="ts">
import { ref } from 'vue'
import { ElButton, ElCard, ElInputNumber, ElTable, ElTableColumn } from 'element-plus'
import { listNeighbors } from '@/api/network/discovery'
const switchId = ref<number>()
const rows = ref<any[]>([])
const load = async () => { if (switchId.value) rows.value = await listNeighbors(switchId.value) }
</script>
<template><div class="p-20px"><ElCard><template #header>Vecinos LLDP/CDP</template><div class="mb-16px flex gap-8px"><ElInputNumber v-model="switchId" placeholder="ID switch" /><ElButton type="primary" @click="load">Consultar</ElButton></div><ElTable :data="rows" border><ElTableColumn prop="id" label="ID" width="70"/><ElTableColumn prop="local_port" label="Puerto local"/><ElTableColumn prop="neighbor_name" label="Vecino"/><ElTableColumn prop="neighbor_ip" label="IP vecina"/><ElTableColumn prop="neighbor_platform" label="Plataforma"/><ElTableColumn prop="neighbor_port" label="Puerto remoto"/><ElTableColumn prop="protocol" label="Protocolo"/></ElTable></ElCard></div></template>
