
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
  },

  {
    path: '/projectsCreating',
    name: 'projects creating',
    component: () => import('../views/ProjectsCreating.vue')
  },

  {
    path: '/admin',
    name: 'admin page',
    component: () => import('../views/AdminView.vue')
  },

  {
    path: '/users',
    name: 'user list',
    component: () => import('../views/UserList.vue')
  },

  {
    path: '/commandCreating/:id',
    name: 'command creating',
    component: () => import('../views/TaskCreating.vue')
  },

  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
