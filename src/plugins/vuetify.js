import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'md'
  },
  theme: {
    themes: {
      light: {
        primary: '#CDDC39',
        secondary: '#4caf50',
        accent: '#ffc107',
        error: '#f44336',
        warning: '#ffeb3b',
        info: '#673ab7',
        success: '#cddc39'
      }
    }
  }
});
