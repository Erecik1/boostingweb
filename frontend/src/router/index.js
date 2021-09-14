import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

import SignUp from '../views/Signup.vue'
import LogIn from '../views/Login.vue'
import Boosters from '../views/Boosters.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: SignUp
  },

  {
    path: '/log-in',
    name: 'Login',
    component: LogIn
  },
      {
    path: '/boosters',
    name: 'Boosters',
    component: Boosters
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
