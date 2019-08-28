<template>
  <v-app>
    <app-navigation></app-navigation>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import AppNavigation from '@/components/AppNavigation';
import Footer from '@/components/Footer';

export default {
  name: 'App',
  components: {
    AppNavigation,
    Footer
  },
  data: () => ({
    //
  })
};
</script>
