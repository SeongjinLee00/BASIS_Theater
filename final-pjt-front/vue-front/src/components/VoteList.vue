<template>
  <div>
    <h5 class="fw-bold mb-3">평점 목록</h5>
    <ul>
      <vote-form></vote-form>
      <vote-list-item :vote="vote">
      </vote-list-item>
    </ul>

    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import VoteListItem from '@/components/VoteListItem'
import VoteForm from '@/components/VoteForm'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { VoteForm, VoteListItem },
  props: { votes: Array },
}
</script>