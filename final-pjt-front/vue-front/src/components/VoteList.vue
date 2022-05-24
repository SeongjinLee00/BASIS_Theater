<template>
  <div>
    <h5 class="fw-bold mb-3">평점 목록</h5>
    <ul>
      <div v-for="vote in votes" :key="vote.pk">
        <vote-list-item :vote="vote">
        </vote-list-item>
      </div>
      <vote-form></vote-form>
    </ul>

  </div>
</template>

<script>
import VoteListItem from '@/components/VoteListItem'
import VoteForm from '@/components/VoteForm'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'VoteList',
  components: { VoteForm, VoteListItem },
  props: { votes: Array },
}
</script>