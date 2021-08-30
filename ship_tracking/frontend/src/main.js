// import BootstrapVue from "bootstrap-vue";  // Import Bootstrap here
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from './plugins/vuetify';
// import 'leaflet/dist/leaflet.css'; 

// Vue.use(BootstrapVue);  
Vue.config.productionTip = false;


new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");