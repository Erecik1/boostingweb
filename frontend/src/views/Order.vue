<template>
  <div class="columns">
  <div class="column is-one-quarter has-text-centered">
    <h2 class="title">Current Tier</h2>
      <div><img :src="leagueImage(startTier)" alt="rank_emblem" width="180" height="205"></div>
  <h2 class="subtitle">Tier</h2>
  <div class="select is-link">
  <select :onchange="calculatePrice" v-model="startTier">
    <option>Iron</option>
    <option>Bronze</option>
    <option>Silver</option>
    <option>Gold</option>
    <option>Platinum</option>
    <option>Diamond</option>
    <option>Master</option>
  </select>
</div>
    <h2 class="subtitle">Division</h2>
    <div class="select is-link">
  <select :onchange="calculatePrice" v-model="startDiv">
    <option>Division 1</option>
    <option>Division 2</option>
    <option>Division 3</option>
    <option>Division 4</option>
  </select>
</div>
  </div>
  <div class="column is-one-quarter has-text-centered">
<h2 class="title">Target Tier</h2>
    <div><img :src="leagueImage(endTier)" alt="rank_emblem" width="180" height="205"></div>
      <h2 class="subtitle">Tier</h2>
    <div class="select is-link">
  <select :onchange="calculatePrice" v-model="endTier">
    <option>Iron</option>
    <option>Bronze</option>
    <option>Silver</option>
    <option>Gold</option>
    <option>Platinum</option>
    <option>Diamond</option>
    <option>Master</option>
  </select>
</div>
  <template v-if="endTier !=='Master'">
    <h2 class="subtitle">Division</h2>
    <div class="select is-link">
  <select :onchange="calculatePrice" v-model="endDiv">
    <option>Division 1</option>
    <option>Division 2</option>
    <option>Division 3</option>
    <option>Division 4</option>
  </select>
      </div>
  </template>
  </div>
    <div class="column is-half" style="border: 1px solid grey;">
      <h1 class="title">Your order</h1>
        <label class="checkbox">
  <input type="checkbox" :onchange="calculatePrice" v-model="isDuo">
  Duo with booster (+35%)
</label>
  <label class="checkbox">
  <input type="checkbox" :onchange="calculatePrice" v-model="isPrio">
  High priority (+20%)
</label>
  <label class="checkbox">
  <input type="checkbox" :onchange="calculatePrice" v-model="isStream">
  Stream games (+10%)
</label>
      <h2 class="subtitle">LP Gain</h2>
          <div class="select is-link">
<select :onchange="calculatePrice" v-model="lpGain">
    <option>1-9</option>
    <option>10-14</option>
    <option>15-18</option>
    <option>19-24</option>
    <option>25+</option>
  </select>
</div>
            <h2 class="subtitle">Your server</h2>
          <div class="select is-link">
<select :onchange="calculatePrice" v-model="accountRegion">
    <option>EUNE</option>
    <option>EUW</option>
    <option>NA</option>
    <option>TR</option>
    <option>RU</option>
  </select>
</div>
      <h2 class="subtitle">Promo code</h2>
      <input class="input" type="text" placeholder="Promo code" maxlength="10">
      <h2 class="subtitle">Order price: $<span>{{price}}</span></h2>
      <button :onclick="sendOrder" class="button is-danger is-light">BUY</button>
          <div id="paypal-button-container"></div>
    </div>
</div>

</template>

<script>
import axios from 'axios'
export default {
  name: "Order",
  data(){
    return{
      data:[],
      startTier:'Bronze',
      startDiv:'Division 4',
      endTier:'Master',
      endDiv:'Division 1',
      accountRegion:'EUW',
      isDuo:false,
      isStream:false,
      isPrio:false,
      price:17,
      srcStart:'',
      srcEnd:'',
      lpGain:'15-18',
    }
  },
  beforeMount() {
    this.calculatePrice()
    document.title = 'Home | Order'
  },
  methods: {
    leagueImage(value) {
      return require('@/assets/rank_icons/Emblem_' + value + '.png')
    },

    calculatePrice() {
      const price_tab = [
    0,
    17,
    17,
    17,
    31,
    17,
    17,
    17,
    31,
    17,
    17,
    17,
    31,
    19,
    19,
    19,
    33,
    26,
    29,
    31,
    52,
    68,
    82,
    116,
    217,]

const rankData = [
    "Iron Division 4",
    "Iron Division 3",
    "Iron Division 2",
    "Iron Division 1",
    "Bronze Division 4",
    "Bronze Division 3",
    "Bronze Division 2",
    "Bronze Division 1",
    "Silver Division 4",
    "Silver Division 3",
    "Silver Division 2",
    "Silver Division 1",
    "Gold Division 4",
    "Gold Division 3",
    "Gold Division 2",
    "Gold Division 1",
    "Platinum Division 4",
    "Platinum Division 3",
    "Platinum Division 2",
    "Platinum Division 1",
    "Diamond Division 4",
    "Diamond Division 3",
    "Diamond Division 2",
    "Diamond Division 1",
    "Master",
]
      this.price = 17
      const data = {
        league_from: this.startTier,
        division_from: this.startDiv,
        league_to: this.endTier,
        division_to: this.endDiv,
        is_duo: this.isDuo,
        is_high_priority: this.isPrio,
        isStream: this.isStream,
        price: this.price,
        lp_gain: this.lpGain,
        account_region: this.accountRegion,
      }
    let multi = 1
    this.data = data
      let target_league = "";
      let starting_league = data.league_from + " " + data.division_from
      if (data.league_to === 'Master'){ target_league = data.league_to }
      else { target_league = data.league_to + " " + data.division_to }
      let count = false
      let leagues = []
      let key = 0
      rankData.every(rank =>{
        key += 1;

        if(count === true){
          leagues.push(key);
        }
        if(starting_league === rank){
          count = true;
        }
        if(target_league === rank){

          return false;
        }
        return true;
      })
    this.price = 0
      leagues.every(league=>{
        this.price += price_tab[league-1];
        return true;
      })
    if (data.is_duo) { multi *= 1.35 }
    if (data.is_high_priority) { multi *= 1.20}
    if (data.isStream) { multi *= 1.10}
    switch (data.lp_gain){
      case "1-9":
        multi *= 1.30;
        break;
      case "10-14":
        multi *= 1.15;
        break;
      case "15-18":
        multi *= 1.0;
        break;
      case "19-24":
        multi *= 0.9;
            break;
      case "25+":
        multi *= 0.75;
            break;
    }
    this.price *= multi
    this.price = this.price.toFixed(2);
    console.log(this.price)
        if(this.price == 0.00){
      this.price = "You can't get deranked"
    }
    },

    sendOrder() {
      if(this.price !== 0.00) {
        axios
            .post('api/v1/orders/', this.data)
            .catch(error => {
              console.log(error)
            })
      }
    }
  },
}

</script>

<style scoped>
.input{
  width: 20%;
}

h2.subtitle{
  margin-bottom: 5px;
  margin-top: 12px;
  color: white;
}
label.checkbox{
  margin-right: 20px;
}
</style>