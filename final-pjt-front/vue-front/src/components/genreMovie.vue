<template>
  <div>
    <div class="box m-1">
      <!-- 글 이동 링크 (제목) -->
      <router-link 
        :to="{ name: 'movie', params: {moviePk: movie.id} }">
        <img id="poster" class="w-100 h-200" :src="poster+movie.poster_path" :alt="movie.title">
      </router-link>
      <!-- <vote-main-form :movie="movie"></vote-main-form> -->
      
    </div>
  </div>
</template>

<script>
// import VoteMainForm from './VoteMainForm.vue'
export default {
  name: 'genreMovie',
  // components: { VoteMainForm },
  props: { movie : Object },
  data() {
    return { 
      poster: "https://image.tmdb.org/t/p/w500",
    }
  },
}
</script>

<style>

</style>