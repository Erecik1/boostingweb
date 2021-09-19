import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    auth_token: '',
  },
  mutations: {
 initializeStore(state) {
   if (localStorage.getItem('Token')) {
    state.auth_token = localStorage.getItem('Token')
    state.isAuthenticated = true
   } else {
    state.auth_token = ''
    state.isAuthenticated = false
   }
 },
  setToken(state, auth_token) {
        state.auth_token = auth_token
        state.isAuthenticated = true
    },
    removeToken(state) {
        state.auth_token = ''
        state.isAuthenticated = false
    },
    },
  actions: {
  },
  modules: {
  }
})
