<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="9">
        <h1 class="text-center">Welcome to 'Whatson-MENA'</h1>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="9">
        <v-list>
          <v-list-item v-for="(auth, id) in allAuths" :key="id">
            <v-list-item-content>{{ auth }}</v-list-item-content>
          </v-list-item>
        </v-list>
        <!-- All Auths: {{allAuths}} -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import MainLayout from '../layouts/MainLayout';
import MainLayoutVue from '../layouts/MainLayout.vue';

export default {
  // data(){
  //   return {
  //     auths: []
  //   }
  // },
  // methods: {
  //   ...mapActions(['getAllAuths'])
  // },
  created() {
    this.$emit(`update:layout`, MainLayoutVue);
  },
  computed: {
    ...mapGetters(['allAuths'])
  }
  // created() {
  //   this.getAllAuths();
  // }
};
</script>
