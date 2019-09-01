<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" light flat>
      <v-toolbar-title class="green--text text--darken-4">Create account</v-toolbar-title>
    </v-toolbar>
    <v-progress-linear v-if="pendingRequest" indeterminate color="secondary"></v-progress-linear>
    <v-card-text>
      <v-form>
        <v-text-field
          v-model="username"
          :error-messages="usernameErrors"
          prepend-icon="person"
          label="User name"
          required
          @input="$v.username.$touch()"
          @blur="$v.username.$touch()"
        ></v-text-field>
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
          :counter="$v.password.$params.minLength.min"
          type="password"
          prepend-icon="lock"
          label="Password"
          required
          @input="$v.password.$touch()"
          @blur="$v.password.$touch()"
        ></v-text-field>
        <v-checkbox
          v-model="termsAgreed"
          :error-messages="termsAgreedErrors"
          :rules="[v => !!v || 'Please read and agree the terms and conditions!']"
          label="Read and agree the terms and conditions"
          required
          @change="$v.termsAgreed.$touch()"
          @blur="$v.termsAgreed.$touch()"
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
      <v-btn color="error" to="/">Cancel</v-btn>
      <v-btn class="green--text text--darken-4" color="primary" @click="createAccount()">Sign-up</v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
import AuthLayout from '../../layouts/AuthLayout';
// import { mapActions } from 'vuex';
// main authorization model
import { Auth } from 'aws-amplify';
// To check the auth status logged in or not
import { AmplifyEventBus } from 'aws-amplify-vue';
// Validation
import { required, minLength, email } from 'vuelidate/lib/validators';
// Special Validation
import {
  hasNumber,
  hasLowerCaseLetter,
  hasUpperCaseLetter,
  hasSpecialCharacter
} from '../../validators/password';

export default {
  data: () => ({
    pendingRequest: false,
    signedIn: false,
    username: '',
    email: '',
    password: '',
    termsAgreed: false
  }),
  validations: {
    username: { required },
    email: { required, email },
    // password: { required, minLength: minLength(8) },
    password: {
      required,
      minLength: minLength(8),
      hasNumber,
      hasLowerCaseLetter,
      hasUpperCaseLetter,
      hasSpecialCharacter
    },
    termsAgreed: {
      checked(val) {
        return val;
      }
    }
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
      this.$v.$touch();
      if (!this.$v.$dirty) {
        this.pendingRequest = true;
        Auth.signUp({
          username: this.email,
          password: this.password,
          attributes: {
            email: this.email,
            name: this.username
          },
          validationData: [] // optional
        })
          .then(data => {
            this.pendingRequest = false;
            this.$router.push({
              path: '/confirmSignup',
              query: { email: this.email }
            });
            console.log(data);
          })
          .catch(err => console.log(err));
      }
    }
  },
  created() {
    this.$emit(`update:layout`, AuthLayout);
    AmplifyEventBus.$on('authState', info => {
      if (info === 'signedIn') {
        console.log(info);
        // this.isUserSignedIn();
        this.signedIn = true;
      } else {
        this.signedIn = false;
      }
    });
  },
  computed: {
    termsAgreedErrors() {
      const errors = [];
      if (!this.$v.termsAgreed.$dirty) return errors;
      !this.$v.termsAgreed.checked &&
        errors.push('You must agree to continue!');
      return errors;
    },
    usernameErrors() {
      const errors = [];
      if (!this.$v.username.$dirty) return errors;
      !this.$v.username.required && errors.push('User name is required.');
      return errors;
    },
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
      !this.$v.password.minLength &&
        errors.push('Password must be at least 8 characters');
      !this.$v.password.hasNumber &&
        errors.push('Password must contain a number');
      !this.$v.password.hasLowerCaseLetter &&
        errors.push('Password must contain lower-case letters');
      !this.$v.password.hasUpperCaseLetter &&
        errors.push('Password must contain upper-case letters');
      !this.$v.password.hasSpecialCharacter &&
        errors.push('Password must contain special character');
      return errors;
    }
  }
};
</script>
