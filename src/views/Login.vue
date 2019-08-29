<template>
  <!-- <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
  <v-col cols="12" sm="8" md="4">-->
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Login</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field label="Login" name="login" type="text" v-model="logData.email"></v-text-field>
        <v-text-field
          id="password"
          label="Password"
          name="password"
          type="password"
          v-model="logData.password"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="lime" @click="login(logData)">Login</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </v-card-actions>
  </v-card>
  <!-- </v-col>
    </v-row>
  </v-container>-->
</template>

<script>
import authLayout from '../layouts/authLayout';
import { mapActions } from 'vuex';

export default {
  data: () => ({
    drawer: null,
    logData: { email: '', password: '' }
  }),
  props: {
    source: String
  },
  methods: {
    ...mapActions(['login'])
  },
  created() {
    this.$emit(`update:layout`, authLayout);
  }
};
</script>
