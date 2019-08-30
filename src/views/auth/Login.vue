<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Login</v-toolbar-title>
    </v-toolbar>
    <v-progress-linear v-if="pendingRequest" indeterminate color="secondary"></v-progress-linear>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Email"
          name="email"
          type="text"
          prepend-icon="email"
          v-model="logData.email"
        ></v-text-field>
        <v-text-field
          id="password"
          label="Password"
          name="password"
          type="password"
          prepend-icon="lock"
          v-model="logData.password"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div>
        <p style="margin: 0">
          <small>
            account?
            <a href="/signup">Signup</a>
          </small>
        </p>
        <p style="margin: 0">
          <small>
            Forget password?
            <a href="/forgetPassword">Reset-password</a>
          </small>
        </p>
      </div>
      <v-spacer></v-spacer>
      <v-btn class="green--text text--darken-4" color="primary" @click="loginUser(logData)">Login</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { Auth } from 'aws-amplify';
import authLayout from '../../layouts/authLayout';
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      pendingRequest: false,
      // drawer: null,
      logData: { email: this.$route.query.email || '', password: '' }
    };
  },
  props: {
    source: String
  },
  methods: {
    ...mapActions(['login']),
    async loginUser(logData) {
      this.pendingRequest = true;
      Auth.signIn(this.logData.email, this.logData.password)
        .then(user => {
          console.log(user);
          this.pendingRequest = false;
          // this.$router.push({path: '/', })
        })
        .catch(err => console.log(err));
    }
  },
  created() {
    this.$emit(`update:layout`, authLayout);
  }
};
</script>
