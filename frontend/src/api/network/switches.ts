import request from '@/axios'
export const listSwitches = () => request.get({ url: '/switches' }) as any
export const createSwitch = (data: any) => request.post({ url: '/switches', data }) as any
export const updateSwitch = (id: number, data: any) => request.put({ url: `/switches/${id}`, data }) as any
export const deleteSwitch = (id: number) => request.delete({ url: `/switches/${id}` }) as any
export const testSsh = (id: number) => request.post({ url: `/switches/${id}/test-ssh` }) as any
