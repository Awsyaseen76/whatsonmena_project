<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="9">
        <h1 class="text-center">Welcome to 'WhatsonMENA'</h1>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="9">
        <v-list>
          <v-list-item v-for="(auth, id) in allAuths" :key="id">
            <v-list-item-content>
              {{ auth }}
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <!-- All Auths: {{allAuths}} -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import http from "../http-common";
import { mapGetters, mapActions } from 'vuex';

export default {
  // data(){
  //   return {
  //     auths: []
  //   }
  // },
  methods: {
    ...mapActions(['getAllAuths'])
  },
  // methods: //{
  // mapActions['getAllAuths'],

  // getAllAuths(){
  //   http
  //     .get('/all')
  //     .then(response => {
  //       this.auths = response.data;
  //       console.log('the auths are: ', response.data);
  //     })
  //     .catch(err => {
  //       console.log(err);
  //     })
  // }
  //},

  computed: {
    ...mapGetters(['allAuths'])
  },

  // mounted(){
  //   this.getAllAuths()
  // },

  created() {
    this.getAllAuths();
  }
};
</script>
