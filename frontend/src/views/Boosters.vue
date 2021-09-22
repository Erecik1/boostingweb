<template>
  <div class="columns">
  <div class="column is-narrow"
       v-for="booster in boostersList"
       v-bind:key="booster.id">
<div class="card">
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-64x64">
          <img class="avatar" :src='booster.profile_image' alt="Boosterimage"/>
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4 is-black"><router-link :to='booster.get_absolute_url'>{{ booster.username }}</router-link></p>
      </div>
    </div>

    <div class="content has-text-centered">
      <div v-if="booster.rank === '1'"><img src="@/assets/rank_icons/Emblem_Master.png" alt="rank_emblem" width="150" height="170"></div>
      <div v-if="booster.rank === '2'"><img src="@/assets/rank_icons/Emblem_Grandmaster.png" alt="rank_emblem" width="150" height="170"></div>
      <div v-if="booster.rank === '3'"><img src="@/assets/rank_icons/Emblem_Challenger.png" alt="rank_emblem" width="150" height="170"></div>
      <p class="subtitle">Languages : {{ booster.languages }}</p>
      <p class="subtitle">Orders done : {{ booster.orders_done }}</p>
      <star-rating :rating="booster.reviews" :read-only="true" :increment="0.1" :show-rating="false"></star-rating>

    </div>
  </div>
</div>
  </div>
    </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
export default {
  name: "Boosters",
  data() {
    return {
      boostersList: [],
    }
  },
  components:{
    StarRating
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
    },
  }
}
</script>

<style scoped>
p{
  color: black;
}
img.avatar {
  border: 5px solid #555;
}
div.card{
  width: 300px;
background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);

}

</style>