<template>
  <div>
    <span class="star">
      ★★★★★
    <span :style="{ width : vote.rate*10 + '%' }" >★★★★★</span></span>
    {{vote.content}}
    
    <div v-if="!isEditing">
      {{ payload.rate}}
      {{ payload.content }} <br>
    </div>
    <div class="text-secondary">
      <span v-if="isEditing">
        <span @input.prevent="starRate" class="star">
        ★★★★★
        <span :style="{ width : starValue }" >★★★★★</span>
        <input type="range" name="rate"  id="rate"  v-model="rate" value="1" step="1" min="0" max="10" required>
        </span><br>
        <label for="content">content: </label>
        <input type="text" id="content" v-model="content">
        <button>vote</button>
        <a @click="onUpdate">Update</a> |
        <a @click="switchIsEditing">Cancle</a>
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
      isEditing: false,
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
    ...mapActions(['updateVote','deleteVote']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
        this.createVote({ moviePk: this.moviePk, rate: this.rate, content: this.content, })
    },
    isVote() {
      if ( this.currentUser.pk === this.votes.user) {
        return this.isVotes
      } else{
        return !this.isVotes
      }
    }
  },

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