<script setup lang="ts">
import { onMounted, onBeforeUnmount } from 'vue'
import { Terminal } from '@xterm/xterm'
import '@xterm/xterm/css/xterm.css'
import { useUserStore } from '@/store/modules/user'
const props = defineProps<{ switchId: number }>()
let socket: WebSocket | null = null
let term: Terminal | null = null
onMounted(() => {
  const token = useUserStore().getToken
  term = new Terminal({ cursorBlink: true, cols: 120, rows: 30 })
  term.open(document.getElementById('ssh-terminal') as HTMLElement)
  term.write('Iniciando SSH...\r\n')
  const wsBase = import.meta.env.VITE_WS_BASE_PATH || 'ws://localhost:8000'
  socket = new WebSocket(`${wsBase}/ws/ssh/${props.switchId}?token=${encodeURIComponent(token)}`)
  socket.onopen = () => term?.write('WebSocket conectado\r\n')
  socket.onmessage = (event) => term?.write(event.data)
  socket.onerror = () => term?.write('\r\n[ERROR] Falló la conexión\r\n')
  socket.onclose = () => term?.write('\r\nSesión finalizada\r\n')
  term.onData((data) => socket?.readyState === WebSocket.OPEN && socket.send(data))
})
onBeforeUnmount(() => { socket?.close(); term?.dispose() })
</script>
<template><div id="ssh-terminal" style="height: 560px; background: #111827; padding: 8px; border-radius: 8px;"></div></template>
