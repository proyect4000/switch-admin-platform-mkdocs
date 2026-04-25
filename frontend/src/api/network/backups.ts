import request from '@/axios'
export const listBackups = (switchId: number) => request.get({ url: `/backups/switches/${switchId}` }) as any
export const runBackup = (switchId: number) => request.post({ url: `/backups/switches/${switchId}/run?backup_type=running-config` }) as any
export const getBackup = (backupId: number) => request.get({ url: `/backups/${backupId}` }) as any
