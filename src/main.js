import Vue from 'vue';
import App from './App.vue'
import router from './router';

// It could be a bad idea to import all components after developing.
// see https://vuematerial.io/getting-started for details.
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';
Vue.use(VueMaterial);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount('#app');
