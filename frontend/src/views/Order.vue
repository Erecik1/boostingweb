<template>
  <div class="columns">
  <div class="column is-one-quarter has-text-centered">
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
      <button :onclick="sendOrder">BUY</button>
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
    calculateDiv(rank1, div1, rank2, div2) {
      const rankData = {
        1: "Iron Division 4",
        2: "Iron Division 3",
        3: "Iron Division 2",
        4: "Iron Division 1",
        5: "Bronze Division 4",
        6: "Bronze Division 3",
        7: "Bronze Division 2",
        8: "Bronze Division 1",
        9: "Silver Division 4",
        10: "Silver Division 3",
        11: "Silver Division 2",
        12: "Silver Division 1",
        13: "Gold Division 4",
        14: "Gold Division 3",
        15: "Gold Division 2",
        16: "Gold Division 1",
        17: "Platinum Division 4",
        19: "Platinum Division 3",
        20: "Platinum Division 2",
        21: "Platinum Division 1",
        22: "Diamond Division 4",
        23: "Diamond Division 3",
        24: "Diamond Division 2",
        25: "Diamond Division 1",
      }
      startRank = rank1 + div1
      endRank = rank2 + div2
      return
    },
    calculatePrice() {
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
    },

    sendOrder() {
      axios
          .post('api/v1/orders/', this.data)
          .catch(error => {
            console.log(error)
          })
    }
  },
}

</script>

<style scoped>
.input{
  width: 20%;
}

</style>