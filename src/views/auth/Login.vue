<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Login</v-toolbar-title>
    </v-toolbar>
    <v-progress-linear v-if="pendingRequest" indeterminate color="secondary"></v-progress-linear>
    <v-card-text>
      <v-form>
        <v-text-field
          v-model="email"
          :error-messages="emailErrors"
          prepend-icon="email"
          label="Email"
          required
          @input="$v.email.$touch()"
          @blur="$v.email.$touch()"
        ></v-text-field>
        <v-text-field
          v-model="password"
          :error-messages="passwordErrors"
          prepend-icon="lock"
          label="Password"
          type="password"
          required
          @input="$v.password.$touch()"
          @blur="$v.password.$touch()"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div>
        <p style="margin: 0">
          <small>
            Don't have account?
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
      <v-btn color="error" to="/">Cancel</v-btn>
      <v-btn class="green--text text--darken-4" color="primary" @click="loginUser()">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { Auth } from 'aws-amplify';
import AuthLayout from '../../layouts/AuthLayout';
import { mapActions } from 'vuex';
import { required, email } from 'vuelidate/lib/validators';

export default {
  data() {
    return {
      pendingRequest: false,
      email: this.$route.query.email || '',
      password: ''
    };
  },
  methods: {
    ...mapActions(['login']),
    async loginUser() {
      this.pendingRequest = true;
      Auth.signIn(this.email, this.password)
        .then(user => {
          console.log(user);
          this.pendingRequest = false;
          this.$router.push({
            path: '/memberProfile',
            query: user
          });
        })
        .catch(err => console.log(err));
    }
  },
  created() {
    this.$emit(`update:layout`, AuthLayout);
  },
  validations: {
    email: { required, email },
    password: { required }
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push('Must be valid e-mail');
      !this.$v.email.required && errors.push('E-mail is required');
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.required && errors.push('Password is required');
      return errors;
    }
  }
};
</script>
