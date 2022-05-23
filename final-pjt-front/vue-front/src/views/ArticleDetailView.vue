<template>
  <div class="container">
    <div class="mb-5">
      <h1>{{ article.title }}</h1>
      <div>
        <div>
          <router-link :to="{ name: 'profile', params: { username } }" class="fw-bold text-black text-decoration-none">
            {{ username }}
          </router-link>
        </div>
        <div>{{article.created_at.substr(0,10)}} {{article.created_at.slice(11,16)}}</div>
      </div>
      <hr>

      <p>
        {{ article.content }}
      </p>
      <!-- Article Edit/Delete UI -->
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button>Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articlePk)">Delete</button>
      </div>

      <div id="authorProfile">
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ username }}님의 게시글 더보기 >>
        </router-link>
      </div>
    </div>
    <!-- Article Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div> -->

    <!-- Comment UI -->
    <p>댓글 {{article.comments.length}}</p>
    <div>
      <comment-list :comments="article.comments"></comment-list>
    </div>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'username']),
      likeCount() {
        return this.article.like_users?.length
      },
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
