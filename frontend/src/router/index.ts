import { createRouter, createWebHashHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import type { App } from 'vue'
import { Layout } from '@/utils/routerHelper'

export const constantRouterMap: AppRouteRecordRaw[] = [
  {
    path: '/',
    component: Layout,
    redirect: '/network/dashboard',
    name: 'Root',
    meta: { hidden: true }
  },
  {
    path: '/login',
    component: () => import('@/views/Login/Login.vue'),
    name: 'Login',
    meta: { hidden: true, title: 'Login', noTagsView: true }
  },
  {
    path: '/404',
    component: () => import('@/views/Error/404.vue'),
    name: 'NoFind',
    meta: { hidden: true, title: '404', noTagsView: true }
  }
]

export const asyncRouterMap: AppRouteRecordRaw[] = [
  {
    path: '/network',
    component: Layout,
    redirect: '/network/dashboard',
    name: 'NetworkAdmin',
    meta: { title: 'Red Institucional', icon: 'vi-ant-design:cluster-outlined', alwaysShow: true },
    children: [
      { path: 'dashboard', component: () => import('@/views/Network/Dashboard/index.vue'), name: 'NetworkDashboard', meta: { title: 'Dashboard', icon: 'vi-ant-design:dashboard-filled', affix: true } },
      { path: 'switches', component: () => import('@/views/Network/Switches/index.vue'), name: 'NetworkSwitches', meta: { title: 'Switches', icon: 'vi-ant-design:database-outlined' } },
      { path: 'topology', component: () => import('@/views/Network/Topology/index.vue'), name: 'NetworkTopology', meta: { title: 'Topología', icon: 'vi-ant-design:deployment-unit-outlined' } },
      { path: 'neighbors', component: () => import('@/views/Network/Neighbors/index.vue'), name: 'NetworkNeighbors', meta: { title: 'Vecinos LLDP/CDP', icon: 'vi-ant-design:branches-outlined' } },
      { path: 'backups', component: () => import('@/views/Network/Backups/index.vue'), name: 'NetworkBackups', meta: { title: 'Backups', icon: 'vi-ant-design:save-outlined' } },
      { path: 'jobs', component: () => import('@/views/Network/Jobs/index.vue'), name: 'NetworkJobs', meta: { title: 'Tareas Programadas', icon: 'vi-ant-design:clock-circle-outlined' } },
      { path: 'history', component: () => import('@/views/Network/History/index.vue'), name: 'NetworkHistory', meta: { title: 'Historial y Auditoría', icon: 'vi-ant-design:history-outlined' } }
    ]
  },
  {
    path: '/security',
    component: Layout,
    redirect: '/security/users',
    name: 'SecurityAdmin',
    meta: { title: 'Seguridad', icon: 'vi-ant-design:safety-certificate-outlined', alwaysShow: true },
    children: [
      { path: 'users', component: () => import('@/views/Security/Users/index.vue'), name: 'SecurityUsers', meta: { title: 'Usuarios', icon: 'vi-ant-design:user-outlined' } },
      { path: 'roles', component: () => import('@/views/Security/Roles/index.vue'), name: 'SecurityRoles', meta: { title: 'Roles y Permisos', icon: 'vi-ant-design:key-outlined' } }
    ]
  },
  { path: '/:path(.*)*', redirect: '/404', name: 'NotFound', meta: { hidden: true } }
]

const router = createRouter({
  history: createWebHashHistory(),
  strict: true,
  routes: constantRouterMap as RouteRecordRaw[],
  scrollBehavior: () => ({ left: 0, top: 0 })
})

export const setupRouter = (app: App<Element>) => {
  app.use(router)
}

export default router
