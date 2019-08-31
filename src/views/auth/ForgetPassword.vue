<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Forgot your password?</v-toolbar-title>
    </v-toolbar>
    <v-progress-linear v-if="pendingRequest" indeterminate color="secondary"></v-progress-linear>
    <v-card-text>
      <v-form>
        <label>Please enter your email to reset your password</label>
        <v-text-field
          label="Email"
          name="email"
          type="text"
          prepend-icon="email"
          v-model="userEmail"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <p>
        <small>
          Back to
          <a href="/login">Login</a>
        </small>
      </p>
      <v-spacer></v-spacer>
      <v-btn
        class="green--text text--darken-4"
        color="primary"
        @click="forgetPassword(userEmail)"
      >Reset-password</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import AuthLayout from '../../layouts/AuthLayout';
import { mapActions } from 'vuex';

export default {
  data: () => ({
    pendingRequest: false,
    // drawer: null,
    userEmail: null
  }),
  props: {
    source: String
  },
  methods: {
    ...mapActions(['login']),
    forgetPassword: userEmail => console.log(userEmail)
  },
  created() {
    this.$emit(`update:layout`, AuthLayout);
  }
};
</script>
