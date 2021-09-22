<style>
  @import './assets/styles/main.css';
</style>
<template>

<div id="wrapper">
<nav class="navbar is-spaced" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src="@/assets/BS_biae.png" alt="logo">
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <div class="navbar-item">
        <router-link to="/" class="navbar-item">Home</router-link>
      </div>

      <div class="navbar-item">
        <router-link to="/boosters" class="navbar-item">Boosters</router-link>
      </div>
      <div v-if="$store.state.isAuthenticated" class="navbar-item">
        <router-link to="/order" class="navbar-item" id="btn-grad">Order</router-link>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <template v-if="$store.state.isAuthenticated">
<div class="dropdown is-hoverable is-right">
  <div class="dropdown-trigger">
    <button class="button" aria-haspopup="true" aria-controls="dropdown-menu4">
      <span>Account</span>
    </button>
  </div>
  <div class="dropdown-menu" id="dropdown-menu4" role="menu">
    <div class="dropdown-content">
      <div class="dropdown-item">
        <router-link to="/my-account" class="dropdown-item">My account</router-link>
        <button @click="logout()" class="dropdown-item">Logout</button>
      </div>
    </div>
  </div>
</div>
        </template>
        <template v-else>
          <router-link to="/log-in" class="navbar-item">Log in</router-link>
        </template>
      </div>
    </div>
  </div>
</nav>

  <section class="section">
    <router-view/>
  </section>
<div style="min-height: 1px;">
</div>
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
</div>
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  methods: {
    logout() {
      axios
      .post("api/v1/token/logout")
      localStorage.removeItem("Token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")
      this.$store.commit('removeToken')
      this.$router.push("/")
    },
  }
}
</script>

<style lang="scss">

#btn-grad {background-image: linear-gradient(to right, #e52d27 0%, #b31217  51%, #e52d27  100%)}
#btn-grad {
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: white;
  box-shadow: 0 0 20px #eee;
  border-radius: 10px;
  display: block;
}

#btn-grad:hover {
  background-position: right center; /* change the direction of the change here */
  color: #fff;
  text-decoration: none;
}

$title-color: hsl(0, 100%, 100%);
//$navbar-padding-vertical: 0.3rem;
$navbar-background-color: rgb(6, 7, 8);
$navbar-height: 2.50rem;
$footer-background-color:rgb(6, 7, 8);
$navbar-item-hover-color: black;
$navbar-item-color: white;
@import '../node_modules/bulma';
</style>
