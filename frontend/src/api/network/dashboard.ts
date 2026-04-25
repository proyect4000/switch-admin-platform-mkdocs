import request from '@/axios'
export const getDashboardSummary = () => request.get({ url: '/dashboard/summary' }) as any
