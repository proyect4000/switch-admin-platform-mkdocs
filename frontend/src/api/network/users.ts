import request from '@/axios'
export const listUsers = () => request.get({ url: '/users' }) as any
export const createUser = (data: any) => request.post({ url: '/users', data }) as any
export const updateUser = (id: number, data: any) => request.put({ url: `/users/${id}`, data }) as any
export const disableUser = (id: number) => request.delete({ url: `/users/${id}` }) as any
export const listRoles = () => request.get({ url: '/roles' }) as any
export const listPermissions = () => request.get({ url: '/roles/permissions' }) as any
