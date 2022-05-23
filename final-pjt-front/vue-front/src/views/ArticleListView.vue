<template>
  <div class="container">
    <img class="w-100" src="../assets/community.jpg" alt="#">
    <div style="height: 1500px;"></div>
    <div class="" id="community">
      <h1 class="">Community</h1>
      <p class="text-end m-3" v-if="isLoggedIn">
        <router-link :to="{ name: 'articleNew' }" class="text-secondary text-decoration-none">New</router-link>
      </p>
      <br>
      <p>총 {{articles.length}}개의 게시물이 있습니다.</p>
      <div class="container" v-for="article in articles" :key="article.pk">
        <hr>
        <div class="m-3">
          <!-- 글 이동 링크 (제목) -->
          <h3>
          <router-link class="fw-bold text-black text-decoration-none"
            :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }} [{{ article.comments.length }}]
          </router-link></h3>
          <div class="my-3">{{article.content.slice(0,20)}}</div>
          <p class="text-secondary ">
          <!-- 작성자 -->
          {{ article.user.username }}
          <!-- 댓글 개수 -->
          | {{article.created_at.substr(0,10)}}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
/* .container {
} */
#community{
  position: sticky;
  height: 800px;
  top: 0;
}
  </style>
