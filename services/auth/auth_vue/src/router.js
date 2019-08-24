import Vue from 'vue';
import Router from 'vue-router';
// import Home from './views/Home.vue';
// import Login from './views/Login';
// import Join from './views/Join';

Vue.use(Router);

// Using lazy loading that load the vues dynamically so it will be faster
const loadview = view => {
  return () =>
    import(/* webpackChunkName: "view-[request]" */ `@/views/${view}.vue`);
};

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/home',
      name: 'home',
      component: loadview('Home')
    },
    {
      path: '/about',
      name: 'about',
      // component: () =>
      //   import(/* webpackChunkName: "about" */ './views/About.vue')
      component: loadview('About')
    },
    {
      path: '/login',
      name: 'login',
      component: loadview('Login')
    },
    {
      path: '/signup',
      name: 'signup',
      component: loadview('Join')
    }
  ]
});
