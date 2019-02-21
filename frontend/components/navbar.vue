<template>
    <nav class="navbar is-transparent is-fixed-top has-navbar-fixed-top is-dark">
      <div id="navbarExampleTransparentExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item" style="margin-left: 30px">
            API Document
          </a>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="field is-grouped" style="margin-right: 30px">
              <div class="field has-addons" style="margin-right: 50px">
                <div class="control">
                  <span class="select">
                    <select>
                      <option>GET</option>
                      <option>POST</option>
                      <option>PUT</option>
                      <option>DELETE</option>
                      <option>PATCH</option>
                    </select>
                  </span>
                </div>
                <div class="control is-expanded">
                  <input class="input" type="text" placeholder="Find the API">
                </div>
                <div class="control">
                  <a class="button is-info">
                    Search
                  </a>
                </div>
              </div>
              <p class="control">
                <a class="button is-primary" v-on:click="addAPI()">
                  <span>
                    Create
                  </span>
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </nav>
</template>
<script>

export default {
  components: {
  },
  methods: {
    addAPI (e) {
      this.$store.dispatch('postApidocs')
    },
  },
  async fetch({ store, params }){
    await store.dispatch('getApidocs')
  }
}
</script>

<style>
</style>
