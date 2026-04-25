import request from '@/axios'
export const runDiscovery = (id: number) => request.post({ url: `/discovery/switches/${id}/run` }) as any
export const listNeighbors = (id: number) => request.get({ url: `/discovery/switches/${id}/neighbors` }) as any
