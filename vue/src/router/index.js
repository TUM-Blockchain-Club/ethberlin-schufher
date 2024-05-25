import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import store from '@/store'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },

    // {
    //   path: '/admin',
    //   name: 'admin',
    //   component: () => import('../views/UserPage.vue'),
    //   meta: { requiresAuth: true }

  ]
})

// auth for the login page
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if authenticated
    if (!store.state.authenticated) {
      // if not, redirect to '/' and show password popout
      next('/')
      store.commit('showPasswordPopOut', { intendedRoute: to })
    } else {
      next() // proceed to route
    }
  } else {
    next() // proceed to route
  }
})

export default router
