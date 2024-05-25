<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div id="app">
      <Auth v-if="showPasswordPopOut" @authenticated="authenticated" />
    <RouterView />
  </div>
</template>

<script>
import Auth from './components/Auth.vue'
import { mapState, mapMutations } from 'vuex'

export default {
  name: 'App',
  components: {
    Auth
  },
  computed: {
    ...mapState(['showPasswordPopOut'])
  },
  methods: {
    ...mapMutations(['authenticate', 'hidePasswordPopOut']),
    authenticated() {
      this.authenticate()
      this.hidePasswordPopOut()
    }
  }
}
</script>
