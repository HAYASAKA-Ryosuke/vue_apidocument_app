<template>
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
</template>

<script>
import { BulmaAccordion, BulmaAccordionItem } from 'vue-bulma-accordion'
export default {
  components: {
    BulmaAccordion,
    BulmaAccordionItem,
  },
  data(){
    return {
      boxMethodColors: {"GET": "is-link", "POST": "is-primary", "PUT": "is-warning", "DELETE": "is-danger"},
    }
  },
  computed:{
    apidocs(){
      return this.$store.state.apidocs
    }
  },
  methods:{
    editAPI (apidoc_id) {
    },
    deleteAPI (apidoc_id) {
    },
    checkAccordionItem(index){
      if (this.$children[0].$children[index].uniqueId == null){
        this.$children[0].$children[index].setUniqueId((index).toString())
        this.$children[0].$children[index].notifyOfClick()
      }
    }
  }
}
</script>
