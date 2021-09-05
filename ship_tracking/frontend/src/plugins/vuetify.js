import Vue from "vue";
import Vuetify from "vuetify/lib/framework";


const colors = {
    kplerOrange: '#ffae42',
    kplerGarnet: '#865900',
    kplerGray40: '#999999',
    kplerBlack: '#000000',
    kplerWhite: '#ffffff',
};

  
Vue.use(Vuetify);

export default new Vuetify({
    theme: {
      themes: {
        light: {
          primary: colors.kplerOrange,
          secondary: colors.kplerWhite,
          black: colors.kplerBlack,
          gray: colors.kplerGray,
          garnet: colors.kplerGarnet,
        },
        dark: {
          primary: colors.kplerOrange,
          secondary: colors.kplerBlack,
          white: colors.kplerWhite,
          gray: colors.kplerGray,
          garnet: colors.kplerGarnet,
        },
      },
  
    },
  });
