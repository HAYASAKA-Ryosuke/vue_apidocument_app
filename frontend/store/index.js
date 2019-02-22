import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import axios from 'axios'
const store = () => new Vuex.Store({
  state: () => ({
    apidocs: null
  }),
  actions: {
    async getApidocs(state){
      axios.get('http://127.0.0.1:8000/apidocs/').then(response => { state.commit('getApidocs', response.data) })
    },
    async postApidocs(state){
      axios.post('http://127.0.0.1:8000/apidocs/', {title: 'ハム作成API', url: 'https://hameggspam/hams/', method: 'POST', description: "# ハムを作るためのAPIです"}).then(response => {  })
      axios.get('http://127.0.0.1:8000/apidocs/').then(response => { state.commit('getApidocs', response.data) })
    },
  },
  mutations: {
    getApidocs(state, value) {
      state.apidocs = value['apidocs']
    },
  }
})
export default store
