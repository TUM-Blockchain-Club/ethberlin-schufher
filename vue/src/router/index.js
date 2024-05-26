import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginPage.vue'),
    },
    {
      path: '/user',
      name: 'user',
      component: () => import('../views/ProfilePage.vue'),
    },
    {
      path: '/application',
      name: 'application',
      component: () => import('../views/Application.vue'),
    },
    {
      path: '/results',
      name: 'results',
      component: () => import('../views/Results.vue'),
      props: true
    }
  ]
})

export default router
