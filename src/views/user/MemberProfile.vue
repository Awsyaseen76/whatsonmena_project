<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="12">
        <h1 class="text-center">Welcome back Champion</h1>
        User name: {{userData.attributes.name}}
        Email: {{userData.attributes.email}}
        signedIn: {{signedIn}}
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DashboardLayout from '../../layouts/DashboardLayout';
import { Auth } from 'aws-amplify';

export default {
  data() {
    return {
      userData: this.$route.query,
      signedIn: true
    };
  },
  methods: {
    async isUserSignedIn() {
      try {
        const userObj = await Auth.currentAuthenticatedUser();
        this.signedIn = true;
        console.log('the user object: ', userObj);
      } catch (error) {
        console.log(error);
        this.signedIn = false;
      }
    }
  },
  created() {
    this.$emit(`update:layout`, DashboardLayout);
    console.log(this.userData);
    this.isUserSignedIn();
  }
};
</script>
