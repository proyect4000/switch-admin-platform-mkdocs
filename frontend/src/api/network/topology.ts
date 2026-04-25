import request from '@/axios'
export const getTopology = () => request.get({ url: '/topology' }) as any
