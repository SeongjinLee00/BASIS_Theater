<template>
<div>
  <!--main -->
  <div id="main" class="my-5" style="text-align:center;">
    <div class="">
      <img class="img-fluid text-center" src="@/assets/mainimg.png" alt="mainImg">
    </div>
  </div>

  <!-- movieList -->
  <div class="container py-5">
    <div>
      <h2>근본영화가 자신있게 추천하는 영화들</h2>
    </div>
    <div class="row">
      <div class="col-3" v-for="movie in movies" :key="movie.pk">
        <div class="box m-1">
          <!-- 글 이동 링크 (제목) -->
          <router-link 
            :to="{ name: 'movie', params: {moviePk: movie.id} }">
            <img id="poster" class="w-100" :src="poster+movie.poster_path" :alt="movie.title">
          </router-link>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import _ from 'lodash'
  export default {
    name: 'MovieList',
    computed: {
      ...mapGetters(['movies']),
      getAction() {
        return _.chunk('movies', 10)
      }
    },
    data() {
      return { 
        poster: "https://image.tmdb.org/t/p/w500",
      }
    },
    methods: {
      ...mapActions(['fetchMovies']),
      randomMain() {
        return _.random(0,70)
      }
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style>
#poster{
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.5s ease-in-out;
}
#poster:hover{
  transform: scale(1.2);
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
}
.box {
  border-radius: 10px;
  overflow: hidden;
}
/* #mainImg{/ */
#mainText{
  font-weight: bold;
  color: rgb(255, 255, 255);
}
</style>
