import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import store from '../store'
import SignUp from '../views/Signup.vue'
import LogIn from '../views/Login.vue'
import Boosters from '../views/Boosters.vue'
import Myaccount from "../views/Myaccount"
import Order from "../views/Order"
import Faq from "../views/Faq"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
  {
    path: '/faq',
    name: 'Faq',
    component: Faq
  },
      {
    path: '/my-account',
    name: 'Myaccount',
    component: Myaccount,
    meta: {
        requireLogin: true
    }
  },
          {
    path: '/order',
    name: 'Order',
    component: Order,
    meta: {
        requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'Login', query: { to: to.path } });
  } else {
    next()
  }
})
export default router
