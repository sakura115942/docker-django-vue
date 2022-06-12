import { createApp } from 'vue'
import App from './App.vue'
import installElementPlus from './plugins/element'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

const app = createApp(App).use(router)
installElementPlus(app)

axios.defaults.baseURL = '/api';
app.use(VueAxios, axios)
app.mount('#app')