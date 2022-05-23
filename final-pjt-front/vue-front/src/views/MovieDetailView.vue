<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <p>
      {{ movie.content }}
    </p>
    <!-- 더 추가해야함 -->
    <vote-form></vote-form>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import VoteForm from '@/components/VoteForm.vue'


  export default {
    name: 'MovieDetail',
    components: { VoteForm },
    data() {
      return {
        moviePk: this.$route.params.moviePk,
      }
    },
    computed: {
      ...mapGetters(['movie']),
    },
    methods: {
      ...mapActions([
        'fetchMovie',
      ])
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style></style>
