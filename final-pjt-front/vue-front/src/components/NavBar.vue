<template>
  <nav class="container">
    <div class="d-flex align-items-center">
      <div class="flex-grow-1">
        <router-link :to="{ name: 'movies' }">근본 영화</router-link>
      </div>

      <div class="" v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </div>
      <div class="" v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </div>

      <div class="m-2" v-if="isLoggedIn">
        <router-link :to="{ name: 'articles' }">Community</router-link>
      </div>
      <div class="m-2" v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link>
      </div>
      <div class="m-2" v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>
@font-face {
    font-family: 'Cafe24SsurroundAir';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/Cafe24SsurroundAir.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
nav {
  font-family: 'Cafe24SsurroundAir';
}
</style>
