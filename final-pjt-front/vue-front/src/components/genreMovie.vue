<template>
<div class="vh-25 vw-25">
  <!-- 글 이동 링크 (제목) -->
  <router-link 
    :to="{ name: 'movie', params: {moviePk: movie.id} }">
    <div id="box" class="">
      <img id="poster" class="h-100 w-100" :src="poster+movie.poster_path" :alt="movie.title">
    </div>
      <h5 class="m-3">{{movie.title}}</h5>
  </router-link>
  </div>        
</template>

<script>
export default {
  name: 'genreMovie',
  props: { movie : Object },
  data() {
    return { 
      poster: "https://image.tmdb.org/t/p/original",
    }
  },
}
</script>

<style>
#box {
  border-radius: 10px;
  overflow: hidden;
  height: 400px;
}
</style>