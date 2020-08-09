import Vue from 'vue';
import axios from 'axios';
import App from './App.vue'
import router from './router';
import store from './store';

// Use axios for API consumption.
Vue.prototype.$http = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  timeout: 5000,
  withCredentials: true
});

// It could be a bad idea to import all components after developing.
// see https://vuematerial.io/getting-started for details.
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';
Vue.use(VueMaterial);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app');
