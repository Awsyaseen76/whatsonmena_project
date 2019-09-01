<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Confirmation code..</v-toolbar-title>
    </v-toolbar>
    <v-progress-linear v-if="pendingRequest" indeterminate color="secondary"></v-progress-linear>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Email"
          name="email"
          type="text"
          prepend-icon="email"
          v-model="userEmail"
          disabled
        ></v-text-field>
        <v-text-field
          id="confirmationCode"
          label="Confirmation code"
          name="confirmationCode"
          type="text"
          prepend-icon="lock"
          v-model="confirmationCode"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <p>
        <small>
          Lost your confirmation code?
          <a href="#">Resend-code</a>
        </small>
      </p>
      <v-spacer></v-spacer>
      <v-btn color="error" to="/">Cancel</v-btn>
      <v-btn
        class="green--text text--darken-4"
        color="primary"
        @click="confirmSignup(confirmationCode)"
      >Confirm</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { Auth } from 'aws-amplify';
import AuthLayout from '../../layouts/AuthLayout';
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      pendingRequest: false,
      confirmationCode: null,
      userEmail: this.$route.query.email,
      // drawer: null,
      logData: { email: '', password: '' }
    };
  },
  props: {
    source: String
  },
  methods: {
    ...mapActions(['login']),
    async confirmSignup(confirmationCode) {
      this.pendingRequest = true;
      Auth.confirmSignUp(this.userEmail, this.confirmationCode, {
        // Optional. Force user confirmation irrespective of existing alias. By default set to True.
        forceAliasCreation: true
      })
        .then(data => {
          console.log(data);
          this.pendingRequest = false;
          this.$router.push({
            path: '/login',
            query: { email: this.userEmail }
          });
        })
        .catch(err => console.log(err));
    }
  },
  created() {
    this.$emit(`update:layout`, AuthLayout);
  }
};
</script>
