import { createStore } from 'vuex';

export default createStore({
  state: {
    banksData: [],
    score: null
  },
  mutations: {
    setBanksData(state, banksData) {
      console.log('Mutating banksData:', banksData); 
      state.banksData = banksData;
    },
    setScore(state, score) {
      console.log('Mutating score:', score); 
      state.score = score;
    }
  },
  actions: {
    updateBanksData({ commit }, banksData) {
      console.log('Dispatching banksData:', banksData); 
      commit('setBanksData', banksData);
    },
    updateScore({ commit }, score) {
      console.log('Dispatching score:', score); 
      commit('setScore', score);
    }
  },
  getters: {
    getBanksData: state => state.banksData,
    getScore: state => state.score
  }
});
