<template>
  <div>
    <amplify-authenticator></amplify-authenticator>
    <amplify-sign-out v-if="signedIn"></amplify-sign-out>
  </div>
  <!-- <v-card class="elevation-12">
    <v-toolbar color="lime" dark flat>
      <v-toolbar-title>Sign-up</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field label="Email" name="Email" type="email" v-model="regData.email"></v-text-field>
        <v-text-field
          id="password"
          label="Password"
          name="password"
          type="password"
          v-model="regData.password"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="lime" @click="register(regData)">Sign-up</v-btn>
      <v-btn color="error" to="/">Cancel</v-btn>
    </v-card-actions>
  </v-card>-->
</template>

<script>
import authLayout from '../layouts/authLayout';
import { mapActions } from 'vuex';
import { Auth } from 'aws-amplify';
import { AmplifyEventBus } from 'aws-amplify-vue';

export default {
  data: () => ({
    signedIn: false,
    drawer: null,
    regData: { email: '', password: '' }
  }),
  props: {
    source: String
  },
  methods: {
    ...mapActions(['register'])
    // async isUserSignedIn() {
    //   try {
    //     const userObj = await Auth.currentAuthenticatedUser();
    //     this.signedIn = true;
    //     console.log('the user object: ', userObj);
    //   } catch (error) {
    //     console.log(error);
    //     signedIn = false;
    //   }
    // }
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
