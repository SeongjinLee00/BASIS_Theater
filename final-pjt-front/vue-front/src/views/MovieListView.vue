<template>
<div>
  <!--main -->
  <div id="main" class="my-5" style="text-align:center;">
    <div class="">
      <img class="img-fluid text-center" src="@/assets/mainImg.png" alt="mainImg">
    </div>
  </div>

  <!-- movieList -->

  <div class="container">
    <div v-for="(genre, name) in movies" :key="genre">
      <h1 class="mt-5">{{name}}</h1>
      <genre-movies :movieList="genre"></genre-movies>
        
    </div>
  </div>
</div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import genreMovies from '../components/genreMovies.vue'

  export default {
    name: 'MovieList',
    components: { genreMovies },
    computed: {
      ...mapGetters(['movies']),
    },
    methods: {
      ...mapActions(['fetchMovies']),
    },
    created() {
      this.fetchMovies()
    },
  }
</script>
