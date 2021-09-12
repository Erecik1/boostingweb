<style>
  @import './assets/styles/main.css';
</style>
<template>

<div id="wrapper">
<nav class="navbar is-spaced" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src="https://pic.onlinewebfonts.com/svg/img_445058.png" width="112" height="28">
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
      <div class="navbar-item">
        <router-link to="/faq" class="navbar-item">Faq</router-link>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
          <router-link to="/log-in" class="navbar-item">Log in</router-link>
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
    <p class="has-text-centered"> This website is not endorsed or in any way affiliated with Activision Inc, Electronic Arts Inc, Valve Corporation, Riot Games Inc, Respawn Entertainment, Bungie, Psyonix Studios or Epic Games and does not reflect the views or opinions of the aforementioned entities or anyone officially involved in producing or managing Overwatch, Fortnite, Call of Duty Franchise, League of Legends, Valorant, Destiny2, World of Warcraft, Rainbow Six Siege, Rocket League, Teamfight Tactics, Dota 2 or Apex Legends. Overwatch, Fortnite, Call of Duty Franchise, League of Legends, Valorant, Destiny2, World of Warcraft, Rainbow Six Siege, Rocket League, Teamfight Tactics, Dota 2 or Apex Legends are trademarks or registered trademarks of the aforementioned entities in the U.S. and/or other countries. All submitted art content remains copyright of its original copyright holder.</p>
  </footer>
</div>
</template>
<script>
export default {
  data(){
    return{
      showMobileMenu: false,
    }
  }
}
</script>

<style lang="scss">
$title-color: hsl(0, 100%, 100%);
//$navbar-padding-vertical: 0.3rem;
$navbar-background-color: rgb(6, 7, 8);
$navbar-height: 2.50rem;
$footer-background-color:rgb(6, 7, 8);
$navbar-item-hover-color: black;
$navbar-item-color: white;
@import '../node_modules/bulma';
</style>
