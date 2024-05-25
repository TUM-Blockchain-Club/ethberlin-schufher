import { createStore } from 'vuex'

export default createStore({
  state: {
    authenticated: false,
    showPasswordPopOut: false
  },
  mutations: {
    authenticate(state) {
      state.authenticated = true;
    },
    showPasswordPopOut(state, payload) {
        state.showPasswordPopOut = true
        state.intendedRoute = payload.intendedRoute
      },
    hidePasswordPopOut(state) {
      state.showPasswordPopOut = false;
    }
  }
})
