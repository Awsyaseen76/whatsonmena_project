<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Create account</v-toolbar-title>
    </v-toolbar>
    <v-progress-linear v-if="pendingRequest" indeterminate color="secondary"></v-progress-linear>
    <v-card-text>
      <v-form>
        <v-text-field
          label="User name"
          name="username"
          type="text"
          prepend-icon="person"
          v-model="regData.username"
        ></v-text-field>
        <v-text-field
          label="Email"
          name="email"
          type="text"
          prepend-icon="email"
          v-model="regData.email"
        ></v-text-field>
        <v-text-field
          id="password"
          label="Password"
          name="password"
          type="password"
          prepend-icon="lock"
          v-model="regData.password"
        ></v-text-field>
        <v-checkbox
          v-model="termsAgreed"
          :rules="[v => !!v || 'Please read and agree the terms and conditions!']"
          label="Read and agree the terms and conditions"
          required
        ></v-checkbox>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <p>
        <small>
          Already have account?
          <a href="/login">Login</a>
        </small>
      </p>
      <v-spacer></v-spacer>
      <v-btn
        class="green--text text--darken-4"
        color="primary"
        @click="createAccount(regData)"
      >Sign-up</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
import authLayout from '../../layouts/authLayout';
// import { mapActions } from 'vuex';
import { Auth } from 'aws-amplify';
import { AmplifyEventBus } from 'aws-amplify-vue';

export default {
  data: () => ({
    pendingRequest: false,
    signedIn: false,
    // drawer: null,
    regData: { username: '', email: '', password: '' },
    termsAgreed: false
  }),
  props: {
    source: String
  },
  methods: {
    // ...mapActions(['register'])
    async isUserSignedIn() {
      try {
        const userObj = await Auth.currentAuthenticatedUser();
        this.signedIn = true;
        console.log('the user object: ', userObj);
      } catch (error) {
        console.log(error);
        signedIn = false;
      }
    },
    async createAccount() {
      this.pendingRequest = true;
      Auth.signUp({
        username: this.regData.email,
        password: this.regData.password,
        attributes: {
          email: this.regData.email,
          name: this.regData.username
        },
        validationData: [] // optional
      })
        .then(data => {
          this.pendingRequest = false;
          this.$router.push({
            path: '/confirmSignup',
            query: { email: this.regData.email }
          });
          console.log(data);
        })
        .catch(err => console.log(err));
    }
  },
  created() {
    this.$emit(`update:layout`, authLayout);
    AmplifyEventBus.$on('authState', info => {
      if (info === 'signedIn') {
        // this.isUserSignedIn();
        this.signedIn = true;
      } else {
        this.signedIn = false;
      }
    });
  }
};
</script>
