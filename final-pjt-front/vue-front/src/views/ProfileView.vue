<template>
  <div>
    <h1>{{ profile.username }}</h1>

    <!-- api 자료 이름 확인 후 변경 예정 -->
    <h2>작성한 평가</h2>
    <ul>
      <li v-for="vote in profile.votes" :key="vote.pk">
        <!-- 평점 및 평가한 영화  -->
        {{ vote.rating }}
        {{ vote.comment }}
        <router-link :to="{ name: 'movie', params: { moviePk: vote.movie.pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>

    <h2>작성한 리뷰</h2>
    <ul>
      <li v-for="review in profile.reviews" :key="review.pk">
        <router-link :to="{ name: 'review', params: { reviewPk: review.pk } }">
          {{ review.title }}
          {{ review.movie_title }}
        </router-link>
      </li>
    </ul>

    <h2>댓글 단 글</h2>
    <ul>
      <li v-for="review in profile.reviews" :key="review.pk">
        <router-link :to="{ name: 'review', params: { reviewPk: review.pk } }">
          {{ review.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
