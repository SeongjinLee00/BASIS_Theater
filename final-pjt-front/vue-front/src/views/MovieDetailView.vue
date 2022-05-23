<template>
  <div>
    <div id="main" class="my-5" style="text-align:center;">
    <div id="movieBox" class="">
      <div id="backImg" class="position-absolute mh-100">
        <img class="img-fluid opacity-25" :src="imgUrl+movie.backdrop_path" alt="#">
      </div>
      <div class="d-flex p-5 justify-content-md-center" id="detailBox">
            <div class="row">
              <img id="posterRow" class="h-100 w-100" :src="imgUrl+movie.poster_path" alt="#">
            </div>
            <div class="text-white col-4 m-5">
              <h1>{{ movie.title }} ({{ movie.release_date.substr(0,4)}})</h1>
              <p>{{ movie.overview.substr(0,250) }}</p>
              <p></p>
            </div>
      </div>
    </div>
    </div>
    <vote-form></vote-form>
  </div>
    <!-- 더 추가해야함 -->
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import VoteForm from '@/components/VoteForm.vue'


  export default {
    name: 'MovieDetail',
    components: { VoteForm },
    computed: {
      ...mapGetters(['movie', 'poster']),
    },
    data() {
      return {
        moviePk: this.$route.params.moviePk,
        imgUrl: `https://image.tmdb.org/t/p/original`,
      }
    },
    methods: {
      ...mapActions([
        'fetchMovie',
      ]),
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style>
#movieBox{
  position: relative;
  height: 500px;
  overflow: hidden;
  background-color: black;
}
#detailBox{
  text-align: left;
  position: absolute;
	display:block;
	width: auto;
	height:500px;
}
#backImg{
  height: 100%;
}
#posterRow{
  border-radius: 30px;
  filter: drop-shadow(10px 10px 10px rgba(0, 0, 0, .8));
  width: 100%;
  height: 100%;
}
</style>
