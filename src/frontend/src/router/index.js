import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/list',
    name: 'projects_list',
    component: () => import('../views/ProjectsList.vue')
  },
    {
    path: '/authorisation',
    name: 'authorisation',
    component: () => import('../views/AuthorisationView.vue')
  },
  
  {
    path: '/registration',
    name: 'reqistration',
    component: () => import('../views/RegistrationView.vue')
  },

  {
    path: '/profile/:id',
    name: 'profile',
    component: () => import('../views/ProfileView.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
