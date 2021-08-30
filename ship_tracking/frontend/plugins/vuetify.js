import Vue from 'vue';
import Vuetify from 'vuetify/lib';

const colors = {
  gmvRed: '#DF0024',
  gmvGarnet: '860015',
  gmvGray40: '#999999',
  gmvBlack: '#000000',
  gmbWhite: '#ffffff',
};

Vue.use(Vuetify);
export default new Vuetify({
  icons: {
    iconfont: 'mdi',
    values: {
      trash: 'mdi-trash-can-outline',
      extent: 'mdi-google-maps',
    },
  },
  theme: {
    themes: {
      light: {
        primary: colors.gmvRed,
        secondary: colors.gmvWhite,
        black: colors.gmvBlack,
        gray: colors.gmvGray,
        garnet: colors.gmvGarnet,
      },
      dark: {
        primary: colors.gmvRed,
        secondary: colors.gmvBlack,
        white: colors.gmbWhite,
        gray: colors.gmvGray,
        garnet: colors.gmvGarnet,
      },
    },

  },
});
