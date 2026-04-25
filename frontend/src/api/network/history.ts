import request from '@/axios'
export const listSessions = () => request.get({ url: '/history/sessions' }) as any
export const listCommands = () => request.get({ url: '/history/commands' }) as any
export const listAuditLogs = () => request.get({ url: '/history/audit-logs' }) as any
