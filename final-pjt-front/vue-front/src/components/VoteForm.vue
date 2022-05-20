<template>
  <form @submit.prevent="onSubmit" class="vote-list-form">
    <label for="vote_rate">vote: </label>
    <input type="range" name="vote_rate" min="0" max="10" id="vote_rate" v-model="vote_rate" required>
    <label for="content">content: </label>
    <input type="text" id="content" v-model="content" required>
    <button>vote</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'VoteForm',
  data() {
    return {
      vote_rate : 0,
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createVote']),
    onSubmit() {
      this.createVote({ moviePk: this.movie.pk, vote_rate: this.vote_rate, content: this.content })
      this.content = ''
    }
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