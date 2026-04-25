<script setup lang="ts">
import { onMounted, reactive } from 'vue'
import { ElCard, ElRow, ElCol, ElStatistic, ElButton } from 'element-plus'
import { useUserStore } from '@/store/modules/user'
import { getDashboardSummary } from '@/api/network/dashboard'

const summary = reactive({ total_switches: 0, online_switches: 0, offline_switches: 0, discovery_success: 0, discovery_error: 0, backups_total: 0 })
const apiBase = import.meta.env.VITE_API_BASE_PATH
const downloadCsv = async () => {
  const token = useUserStore().getToken
  const res = await fetch(`${apiBase}/reports/switches.csv`, { headers: { Authorization: `Bearer ${token}` } })
  const blob = await res.blob()
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'switches.csv'
  a.click()
  window.URL.revokeObjectURL(url)
}
const load = async () => Object.assign(summary, await getDashboardSummary())
onMounted(load)
</script>
<template>
  <div class="p-20px">
    <h2>Dashboard Ejecutivo de Red</h2>
    <ElRow :gutter="16">
      <ElCol :span="8"><ElCard><ElStatistic title="Total switches" :value="summary.total_switches" /></ElCard></ElCol>
      <ElCol :span="8"><ElCard><ElStatistic title="Online" :value="summary.online_switches" /></ElCard></ElCol>
      <ElCol :span="8"><ElCard><ElStatistic title="Offline" :value="summary.offline_switches" /></ElCard></ElCol>
      <ElCol :span="8" class="mt-16px"><ElCard><ElStatistic title="Discovery OK" :value="summary.discovery_success" /></ElCard></ElCol>
      <ElCol :span="8" class="mt-16px"><ElCard><ElStatistic title="Discovery Error" :value="summary.discovery_error" /></ElCard></ElCol>
      <ElCol :span="8" class="mt-16px"><ElCard><ElStatistic title="Backups" :value="summary.backups_total" /></ElCard></ElCol>
    </ElRow>
    <ElCard class="mt-16px">
      <ElButton type="primary" @click="downloadCsv">Exportar switches CSV</ElButton>
    </ElCard>
  </div>
</template>
