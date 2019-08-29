<template>
  <div>
    <app-navigation></app-navigation>
    <v-content>
      <slot />
    </v-content>
    <Footer></Footer>
  </div>
</template>

<script>
import AppNavigation from '@/components/AppNavigation';
import Footer from '@/components/Footer';

export default {
  components: {
    AppNavigation,
    Footer
  }
};
</script>