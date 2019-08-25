<template>
  <div>
    <v-toolbar class="lime">
      <v-app-bar-nav-icon v-if="$vuetify.breakpoint.smAndDown" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer class="hidden-md-and-up"></v-spacer>
      <v-toolbar-title class="green--text text--darken-4">
        {{
        appTitle
        }}
      </v-toolbar-title>
      <v-spacer class="hidden-sm-and-down"></v-spacer>
      <template v-if="$vuetify.breakpoint.mdAndUp">
        <!-- <v-toolbar-items  v-for="(item, index) in items" :key='index' class="green--text text--darken-4">
                    <v-tab :to="item.title" active-class="white--text">{{item.title}}</v-tab>
        </v-toolbar-items>-->
        <v-toolbar-items class="green--text text--darken-4">
          <v-tab active-class="white--text" :to="'home'">Home</v-tab>
          <v-tab active-class="white--text" :to="'about'">About</v-tab>
          <v-tab active-class="white--text" :to="'login'" v-if="!loggedin">Login</v-tab>
          <v-tab active-class="white--text" :to="'signup'" v-if="!loggedin">Register</v-tab>
          <v-tab active-class="white--text" v-if="loggedin">
            {{
            loggedin.id
            }}
          </v-tab>
        </v-toolbar-items>
      </template>
    </v-toolbar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav>
        <v-list-item-group v-model="group" active-class="green--text text--darken-4">
          <v-list-item v-for="(item, index) in items" :key="index" display="block">
            <v-list-item-content>
              <router-link :to="item.title">
                <v-list-item-title class="text-center green--text text--accent-4">{{ item.title }}</v-list-item-title>
              </router-link>
            </v-list-item-content>
          </v-list-item>
          <v-list-item
            class="text-center green--text text--accent-4"
            display="block"
            active-class="green--text text--darken-4"
            v-if="loggedin"
          >{{ loggedin.id }}</v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: 'AppNavigation',
  data() {
    return {
      appTitle: 'WhatsonMENA',
      drawer: false,
      group: null,
      items: [
        { title: 'home' },
        { title: 'about' },
        { title: 'login' },
        { title: 'signup' }
      ]
    };
  },
  watch: {
    group() {
      this.drawer = false;
    }
  },
  computed: {
    ...mapGetters(['loggedin'])
  }
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
