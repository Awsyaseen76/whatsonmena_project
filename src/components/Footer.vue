<template>
  <v-footer dark padless fixed>
    <v-card class="flex" flat tile>
      <v-card-title class="lime">
        <v-row v-for="icon in icons" :key="icon" class="md-4" dark icon justify="center">
          <v-tab>
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-tab>
        </v-row>
      </v-card-title>

      <v-card-actions class="secondary lighten-2 justify-center">
        <small>{{ new Date().getFullYear() }} WHATSONMENA</small>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-instagram',
        'mdi-linkedin',
        'mdi-whatsapp',
        'mdi-youtube',
        'mdi-snapchat'
      ]
    };
  }
};
</script>
