<template>
  <div class="container">
    <div class="row">
    <h1 class="col">Community</h1>
    <p class="col text-end m-3" v-if="isLoggedIn">
      <router-link :to="{ name: 'articleNew' }" class="text-secondary text-decoration-none">New</router-link>
    </p>
    </div>
    <br>
    <p>총 {{articles.length}}개의 게시물이 있습니다.</p>
    <div>
      <ul class="list-group">
        <li class="list-group-item" v-for="article in articles" :key="article.pk">
          
          <!-- 글 이동 링크 (제목) -->
          <router-link class="fw-bold text-black text-decoration-none"
            :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }} [{{ article.comment_count }}]
          </router-link>
          <p class="text-secondary ">
          <!-- 작성자 -->
          {{ article.user.username }}
          <!-- 댓글 개수/좋아요 개수 -->
          | {{ article.like_count }}
          {{article.created_at.substr(0,10)}}
          </p>
        </li>
      </ul>
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

<style></style>
