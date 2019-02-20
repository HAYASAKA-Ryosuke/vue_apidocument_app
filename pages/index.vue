<template>
  <section class="container">
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
    <BulmaAccordion
        dropdown
        :icon="'caret'"
        :caretAnimation="{
            duration: '.2s',
            timerFunc: 'ease-in-out'
        }"
        :slide="{
            duration: '.2s',
            timerFunc: 'ease'
        }"
        style='padding-top: 80px; padding-left: 40px; padding-right: 40px;'
    >
        <div  v-on:click="checkAccordionItem(index)" v-for="(apidoc, index) in apidocs" :key=index >
          <BulmaAccordionItem>
              <h4 slot="title"><span class="tag" v-bind:class="[boxMethodColors[apidoc.method]]">{{ apidoc.method }}</span><strong>{{apidoc.url}}</strong><p>{{ apidoc.description }}</p></h4>
              <div class="content is-1" slot="content" v-html="$md.render(apidoc.description)"></div>
          </BulmaAccordionItem>
        </div>
    </BulmaAccordion>
  </section>
</template>

<script>
import axios from 'axios'
import { BulmaAccordion, BulmaAccordionItem } from 'vue-bulma-accordion'

export default {
  components: {
    BulmaAccordion,
    BulmaAccordionItem,
  },
  data(){
      return {
        apidocs: null,
        boxMethodColors: {"GET": "is-link", "POST": "is-primary", "PUT": "is-warning", "DELETE": "is-danger"},
      }
  },
  asyncData({context}) {
    return axios.get('http://127.0.0.1:8000/apidocs/').then(response => { return response.data })
  },
  methods: {
    addAPI (e) {
      axios.post('http://127.0.0.1:8000/apidocs/', {url: 'test!!', method: 'GET', description: "# ham\n## egg"}).then(response => {  })
      axios.get('http://127.0.0.1:8000/apidocs/').then(response => { this.apidocs = response.data['apidocs'] })
      let children_length = this.$children[0].$children.length
      this.$children[0].$children[children_length - 1].setUniqueId((this.apidocs.length - 1).toString())
    },
    editAPI (apidoc_id) {
    },
    deleteAPI (apidoc_id) {
    },
    checkAccordionItem(index){
        if (this.$children[0].$children[index].uniqueId == null){
          this.$children[0].$children[index].setUniqueId((this.apidocs.length - 1).toString())
          this.$children[0].$children[index].notifyOfClick()
        }
    }
  }
}
</script>

<style>
</style>
