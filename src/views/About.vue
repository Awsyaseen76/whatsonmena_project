<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="9">
        <h1 class="text-center">This is about page</h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MainLayout from '../layouts/MainLayout';

export default {
  created() {
    this.$emit(`update:layout`, MainLayout);
  }
};
</script>