<template>
  <div class="container">
    <h1 class="mt-5">로그인</h1>
    <!-- authError값이 있을 경우만 보여준다 -->
    <div class="alert alert-danger" v-if="authError" role="alert">
      <account-error-list nt-error-list ></account-error-list>
    </div>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">아이디: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>

      <div>
        <label for="password">비밀번호: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>
      <button>Login</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components : {
    AccountErrorList,
  },
  data() {
    return {
      // v-model로 받아서 login으로 넘겨줌
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed : {
    ...mapGetters(['authError'])
  },
  methods : {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>