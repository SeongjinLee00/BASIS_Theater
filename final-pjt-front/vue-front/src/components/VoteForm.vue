<template>
  <form @submit.prevent="onSubmit" class="vote-list-form">
    <label for="rate">vote: </label>
    <input type="range" name="rate" min="0" max="10" id="rate" v-model="rate" required>
    <label for="content">content: </label>
    <input type="text" id="content" v-model="content">
    <button>vote</button>
  </form>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'VoteForm',
  data() {
    return {
      rate : 0,
      content: '',
      moviePk: 0,
    }
  },
  computed: {
    ...mapGetters(['movie','currentUser']),
  },
  methods: {
    ...mapActions(['createVote']),
    getMovie() {
      if ( _.isEmpty(this.movie)) {
        this.moviePk = this.$attrs.movie.id
      } else {
        this.moviePk = this.movie.id
      }

    },
    onSubmit() {
      this.createVote({ moviePk: this.moviePk, rate: this.rate, content: this.content, })
    }
  },
  created() {
    this.getMovie()
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>