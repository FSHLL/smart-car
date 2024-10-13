import { createApp } from 'vue'
import axios from 'axios';
import Antd from 'ant-design-vue';
import App from './App.vue'
import 'ant-design-vue/dist/reset.css';
import { createPinia } from 'pinia';

const pinia = createPinia()
const app = createApp(App);

app.use(pinia)
app.use(Antd)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend

app.mount('#app');
