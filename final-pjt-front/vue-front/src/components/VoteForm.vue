<template>
  <form @click.prevent="onSubmit" class="vote-list-form">
    <span @input.prevent="startRate" class="star">
    ★★★★★
    <span :style="{ width : starValue }" >★★★★★</span>
    <input type="range" name="rate"  id="rate"  v-model="rate" value="1" step="1" min="0" max="10" required>
    </span><br>
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
      starValue: 0,
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
    },
    startRate() {
      this.starValue = this.rate*10 + '%'
    },
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
  .star {
    position: relative;
    font-size: 2rem;
    color: #ddd;
  }
  
  .star input {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    opacity: 0;
    cursor: pointer;
  }
  
  .star span {
    width: 0;
    position: absolute; 
    left: 0;
    color: red;
    overflow: hidden;
    pointer-events: none;
  }
</style>