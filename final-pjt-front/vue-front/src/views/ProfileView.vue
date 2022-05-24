<template>
  <div class="container">
    <div class="my-5">
      <h1>{{ profile.profile.username }}님, 반가워요!</h1>
      <p class="text-secondary">평가영화 {{ profile.votesCount }} | 작성글 {{ profile.articles }}</p>

      <div class="mt-3">
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
      </div>

      <div class="mt-5">
        <h3 v-if="profile.articles">작성한 글</h3>
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
      </div>

    </div>
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
