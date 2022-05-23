<template>
  <div class="container">
    <h1>{{ profile.username }}</h1>
    <p class="text-secondary">평가영화 {{ votesCount }} | 작성글 {{ articlesCount }}</p>

    <!-- api 자료 이름 확인 후 변경 예정 -->
    <h3 v-if="profile.votes">작성한 평가</h3>
    <ul>
      <li v-for="vote in profile.votes" :key="vote.pk">
        <!-- 평점 및 평가한 영화  -->
        {{ vote.rating }}
        {{ vote.comment }}
        <router-link :to="{ name: 'movie', params: { moviePk: vote.movie_pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>

    <h3 v-if="profile.articles">작성한 리뷰</h3>
    <ul class="list-group">
      <li v-for="article in profile.articles" :key="article.pk" class="list-group-item">
        <div class="container">
          <div class="row">
            <div class="col">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }" class="text-black text-decoration-none">
              {{ article.title }}
            </router-link></div>
            <div class="col text-end text-secondary">{{article.created_at.substr(0,10)}}</div>
          </div>
        </div>
      </li>
    </ul>
    <!-- <h2>댓글 단 글</h2>
    <ul>
      <li v-for="comment in profile.comments" :key="comment.pk">
        <router-link :to="{ name: 'article', params: { articlePk: comment.article_pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile']),
    articlesCount() {
      if (this.profile.articles) {
        return this.profile.articles?.length
      } else {
        return 0
      }
    },
    votesCount() {
      if (this.profile.votes) {
        return this.profile.votes?.length
      } else {
        return 0
      }
    },
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
