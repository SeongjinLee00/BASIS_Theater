<template>
  <div class="container">
    <!-- <h1 class="my-5">{{recommend.message}}</h1> -->
    <div class="row">
      <div class="col-4" v-for="movie in recommend.recommended_movies" :key="movie.pk">
        <router-link 
          :to="{ name: 'movie', params: {moviePk: movie.id} }">
          <div class="box">
            <img id="posterRow" class="h-100 w-100" :src="imgUrl+movie.poster_path" alt="#">
          </div>
          <div class="d-flex m-3">
            <div class="row align-self-center mx-3">{{movie.title}}({{movie.release_date.slice(0,4)}})</div>
            <div class="row mx-3 btn btn-danger" type="button">
              {{movie.average_rate}}점
            </div>
          </div>
        </router-link>
        <div class="d-flex">
          <div class="d-inline-flex btn btn-light mb-2 me-1" type="button" v-for="genre in movie.genre_ids" :key="genre.pk">
            {{genre.name}}
          </div>
        </div>
        {{movie.overview.slice(0,200)}}
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieRecommendation',
  data() {
    return {
      imgUrl: `https://image.tmdb.org/t/p/original`,
    }
  },
  computed: {
    ...mapGetters(['recommend']),
  },
  methods : {
    ...mapActions(['fetchRecommend'])
  },
  created() {
      this.fetchRecommend()
  },
}
</script>

<style>
#posterRow{
  border-radius: 30px;
  width: 100%;
  height: 100%;
}
</style>