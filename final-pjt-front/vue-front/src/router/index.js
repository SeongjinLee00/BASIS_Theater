import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'

import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieNewView from '@/views/MovieNewView'
import MovieEditView from '@/views/MovieEditView'

import CommunityListView from '@/views/CommunityListView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import CommunityNewView from '@/views/CommunityNewView'
import CommunityEditView from '@/views/CommunityEditView'


Vue.use(VueRouter)

const routes = [
  // accounts
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  // movies
  {
    path: '/', // HOME
    name: 'movies',
    component: MovieListView,
  },
  {
    path: '/movies/new',
    name: 'movieNew',
    component: MovieNewView,
  },
  {
    path: '/movies/:moviePk',
    name: 'movie',
    component: MovieDetailView,
  },
  {
    path: 'movies/:moviePk/edit',
    name: 'MovieEdit',
    component: MovieEditView,
  },
  // communities
  {
    path: '/communities',
    name: 'communities',
    component: CommunityListView,
  },
  {
    path: '/communities/new',
    name: 'communityNew',
    component: CommunityNewView,
  },
  {
    path: '/communities/:communityPk',
    name: 'community',
    component: CommunityDetailView,
  },
  {
    path: '/communities/:communityPk/edit',
    name: 'communityEdit',
    component: CommunityEditView,
  },
  // etc
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
/*
Navigation Guard 설정
  (이전 페이지에서 있던 에러 메시지 삭제)

  로그인(Authentication)이 필요 없는 route 이름들 저장(/login, /signup)

  0. router 에서 이동 감지

  1. 현재 이동하고자 하는 페이지가 로그인이 필요한지 확인
  
  2. 로그인이 필요한 페이지인데 로그인이 되어있지 않다면
    로그인 페이지(/login)로 이동

  3. 로그인이 되어 있다면
    원래 이동할 곳으로 이동
  
  4. 로그인이 되어있는데 /login, /signup 페이지로 이동한다면
    메인 페이지(/)로 이동
    

*/

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러msg 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.gettters
  // 인증이 필요없는 페이지들
  const noAuthPages = [ 'login', 'signup' ]

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn ) {
    alert('로그인이 필요합니다')
    next({name: 'login'})
  } else {
    next()
  }

  // 로그인 되어있는데 login이나 signup으로가면 main 페이지로 이동
  if (!isAuthRequired && !isLoggedIn) {
    next({name: 'movies'})
  }
})



export default router
