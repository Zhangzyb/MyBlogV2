import Vue from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'

import 'assets/icons/iconfont.css'

import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'

Vue.prototype.$bus = new Vue()

Vue.use(VueSweetalert2)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: function (h) { return h(App) },
}).$mount('#app')
