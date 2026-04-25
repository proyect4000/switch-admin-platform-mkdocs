export interface UserLoginType {
  username: string
  password: string
}

export interface UserType {
  id?: number
  username: string
  password?: string
  full_name?: string
  email?: string
  role: string
  roleId?: string
}
