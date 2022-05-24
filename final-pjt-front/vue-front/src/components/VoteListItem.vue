<template>
  <div>
    
    <div v-if="!isEditing">
      <span class="star">
        ★★★★★
      <span :style="{ width : vote.rate*10 + '%' }" >★★★★★</span></span>
      {{vote.content}}
      {{ payload.rate}}
      {{ payload.content }} <br>
    </div>
    <div class="text-secondary">
      <span v-if="isEditing">
        <span @input.prevent="starRate" class="star">
        ★★★★★
        <span :style="{ width : starValue }" >★★★★★</span>
        <input type="range" name="rate"  id="rate"  v-model="rate" value="1" step="1" min="0" max="10">
        </span><br>
        <label for="content">content: </label>
        <input type="text" id="content" v-model="content">
        <a @click="onUpdate"
        onmouseover="this.style.color='orange';" onmouseout="this.style.color='';">Update</a> |
        <a @click="switchIsEditing"
        onmouseover="this.style.color='orange';" onmouseout="this.style.color='';">Cancle</a>
      </span>
      <span v-if="currentUser.pk === vote.user && !isEditing">
        <a @click="switchIsEditing"
        onmouseover="this.style.color='orange';" onmouseout="this.style.color='';">
        Edit</a> |
        <a @click="deleteVote(payload)"
        onmouseover="this.style.color='orange';" onmouseout="this.style.color='';">
        Delete</a>
      </span>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import VoteForm  from '../components/VoteForm.vue'

export default {
  name: "VoteListItem",
  conponents: {VoteForm},
  props: { vote : Object },
  data() {
    return {
      moviePk: this.vote.movie,
      rate: this.vote.rate,
      content: this.vote.content,
      isEditing: false,
      myVote: 0,
      starValue: '',
      v: 0,
      
      payload: { 
        moviePk: this.vote.movie,
        votePk: this.vote.id,
        rate: this.vote.rate,
        content: this.vote.content,
      }
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['createVote','deleteVote','setVote',]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
        this.createVote({ moviePk: this.moviePk, rate: this.rate, content: this.content,})
        this.isEditing = false
    },
    isVote() {
      if ( this.currentUser.pk === this.vote.user) {
        this.myVote = this.vote.rate
        this.v = this.setVote(this.myVote)
      }
    },
    starRate() {
      this.starValue = this.rate*10 + '%'
    },
  },
  created() {
    this.isVote()
  }

}
</script>

<style>

  .star {
    position: relative;
    font-size: 2rem;
    color: #ddd;
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