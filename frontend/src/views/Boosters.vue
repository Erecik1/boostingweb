<template>
  <div class="columns">
  <div class="column is-one-third"
       v-for="booster in boostersList"
       v-bind:key="booster.id">
<div class="card">
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img :src='booster.profile_image' alt="Boosterimage"/>
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4 is-black">{{ booster.username }}</p>
      </div>
    </div>

    <div class="content">
      <p class="subtitle">BIO:{{ booster.about }}</p>
      <p class="subtitle">Rank:{{ booster.rank }}</p>
      <p class="subtitle">Orders done:{{ booster.orders_done }}</p>
      <p class="subtitle">Reviews ratio:{{ booster.reviews }}</p>
      <p class="subtitle">Active:{{ booster.status }}</p>
      <p class="subtitle">Languages:{{ booster.languages }}</p>
    </div>
  </div>
</div>
  </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Boosters",
  data(){
    return{
      boostersList: []
    }
  },
  components:{
  },
  beforeMount() {
    this.getBoostersList()
    document.title = 'Home | Boost'
  },
  methods:{
    getBoostersList(){
      axios
      .get('/api/v1/boosters-list/')
      .then(response=>{
        this.boostersList = response.data
      })
      .catch(error =>{
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
p{
  color: black;
}

</style>