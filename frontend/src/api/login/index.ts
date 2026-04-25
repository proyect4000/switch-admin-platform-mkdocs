import request from '@/axios'
import type { UserLoginType } from './types'

export const loginApi = (data: UserLoginType): Promise<any> => {
  const form = new URLSearchParams()
  form.append('username', data.username)
  form.append('password', data.password)
  return request.post({
    url: '/auth/login',
    data: form,
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  }) as any
}

export const loginOutApi = (): Promise<any> => {
  return Promise.resolve({ data: true })
}

export const getMeApi = (): Promise<any> => {
  return request.get({ url: '/auth/me' }) as any
}

export const getUserListApi = ({ params }: AxiosConfig) => {
  return request.get({ url: '/users', params }) as any
}

export const getAdminRoleApi = (): Promise<any> => {
  return request.get({ url: '/roles' }) as any
}

export const getTestRoleApi = (): Promise<any> => {
  return request.get({ url: '/roles' }) as any
}
