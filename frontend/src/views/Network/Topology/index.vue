<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { ElButton, ElCard, ElDialog, ElMessage } from 'element-plus'
import { Network } from 'vis-network/standalone'
import { getTopology } from '@/api/network/topology'
import { runDiscovery } from '@/api/network/discovery'
import SshTerminal from '../components/SshTerminal.vue'

const selected = ref<any>(null)
const terminal = ref(false)
let network: Network | null = null
let latest: any = null
const load = async () => {
  latest = await getTopology()
  const container = document.getElementById('network-map') as HTMLElement
  network?.destroy()
  network = new Network(container, latest, {
    physics: { enabled: true },
    interaction: { hover: true },
    nodes: { shape: 'box', margin: 12 },
    edges: { smooth: true, font: { align: 'middle' } },
    groups: {
      online: { color: { background: '#dcfce7', border: '#16a34a' } },
      offline: { color: { background: '#fee2e2', border: '#dc2626' } },
      unknown: { color: { background: '#e5e7eb', border: '#6b7280' } }
    }
  })
  network.on('click', (params: any) => {
    if (params.nodes.length) selected.value = latest.nodes.find((n: any) => n.id === params.nodes[0])
  })
}
const discover = async () => { if (!selected.value) return; const r = await runDiscovery(selected.value.id); ElMessage.success(r.summary); await load() }
onMounted(load)
</script>
<template>
  <div class="p-20px">
    <ElCard>
      <template #header><div class="flex justify-between"><span>Mapa de Topología</span><ElButton @click="load">Recargar</ElButton></div></template>
      <div class="flex gap-16px">
        <div id="network-map" style="height: 720px; flex: 1; border: 1px solid #dcdfe6; border-radius: 8px;"></div>
        <ElCard v-if="selected" style="width: 320px">
          <h3>Switch seleccionado</h3>
          <p><b>ID:</b> {{ selected.id }}</p>
          <p style="white-space: pre-line"><b>Equipo:</b> {{ selected.label }}</p>
          <ElButton type="primary" class="w-full mb-8px" @click="terminal=true">Abrir consola SSH</ElButton>
          <ElButton type="success" class="w-full" @click="discover">Ejecutar discovery</ElButton>
        </ElCard>
      </div>
    </ElCard>
    <ElDialog v-model="terminal" title="Consola SSH" width="90%" destroy-on-close><SshTerminal v-if="selected" :switch-id="selected.id" /></ElDialog>
  </div>
</template>
