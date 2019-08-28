// import http from '../../glue';

const state = {
  allAuths: [1, 2, 3],
  logged: undefined
};

const getters = {
  allAuths: state => state.allAuths,
  loggedin: state => state.logged
};

// const actions = {
//   async getAllAuths({ commit }) {
//     try {
//       const response = await http.get('/all');
//       commit('setAuths', response.data);
//       console.log(response);
//     } catch (error) {
//       console.log(error);
//     }
//   },
//   async register({ commit }, regData) {
//     try {
//       const response = await http.post('/create_auth', regData);
//       console.log(response);
//       commit('setLogged', response.data);
//     } catch (error) {
//       console.log(error);
//     }
//   },
//   async login({ commit }, logData) {
//     try {
//       const loggedAuth = await http.post('/login', logData);
//       console.log(loggedAuth.data);
//       commit('setLogged', loggedAuth.data);
//     } catch (error) {
//       console.log(error);
//     }
//   }
// };

// const mutations = {
//   setAuths: (state, auths) => (state.allAuths = auths),
//   setLogged: (state, auth) => (state.logged = auth)
// };

export default {
  state,
  getters
  // actions,
  // mutations
};
