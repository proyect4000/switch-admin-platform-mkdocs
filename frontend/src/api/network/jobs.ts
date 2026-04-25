import request from '@/axios'
export const listJobs = () => request.get({ url: '/jobs' }) as any
export const createJob = (data: any) => request.post({ url: '/jobs', data }) as any
export const toggleJob = (id: number) => request.put({ url: `/jobs/${id}/toggle` }) as any
