const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMENTS = 'comments/'
const COMMUNITIES = 'communities/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    comments: moviePk => HOST + MOVIES + `${moviePk}/` + COMMENTS,
    comment: (moviePk, commentPk) =>
      HOST + MOVIES + `${moviePk}/` + COMMENTS + `${commentPk}/`,
  },
  communities: {
    communities : () => HOST + COMMUNITIES,
    community: communityPk => HOST + COMMUNITIES + `${communityPk}/`,
    comments: communityPk => HOST + COMMUNITIES + `${communityPk}/` + COMMENTS + `${commentPk}`,
  }
}
