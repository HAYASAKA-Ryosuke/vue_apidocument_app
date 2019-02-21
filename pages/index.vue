<template>
  <section class="container">
    <navbar />
    <apiDoc />
  </section>
</template>

<script>
import axios from 'axios'
import navbar from '~/components/navbar'
import apiDoc from '~/components/apiDoc'

export default {
  components: {
    navbar,
    apiDoc,
  },
  async fetch({ store, params }){
    await store.dispatch('getApidocs')
  }
}
</script>

<style>
</style>
