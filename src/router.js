import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import About from './views/About';
import Login from './views/auth/Login';
import Signup from './views/auth/Signup';
import ConfirmSignup from './views/auth/ConfirmSignup.vue';
import ForgetPassword from './views/auth/ForgetPassword.vue';
import MemberProfile from './views/user/MemberProfile.vue';

Vue.use(Router);

// Using lazy loading that load the vues dynamically so it will be faster
// const loadview = view => {
//   return () =>
//     import(/* webpackChunkName: "view-[request]" */ `@/views/${view}.vue`);
// };

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
      // component: loadview('Home')
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/confirmSignup',
      name: 'confirmSignup',
      component: ConfirmSignup
    },
    {
      path: '/forgetPassword',
      name: 'forgetPassword',
      component: ForgetPassword
    },
    {
      path: '/memberProfile',
      name: 'memberProfile',
      component: MemberProfile
    }
  ]
});
