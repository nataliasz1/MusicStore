import Vue from 'vue'
import App from './App.vue'
import {BootstrapVue, BootstrapVueIcons} from "bootstrap-vue";
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueRouter from 'vue-router'
import Home from "@/components/Home";
import Product from "@/components/Product";
import Cart from "@/components/Cart";
import SearchResults from "@/components/SearchResults";
import Login from "@/components/Login";
import VueSession from 'vue-session'
import Profile from "@/components/Profile";
import Payment from "./components/Payment";
import Order from "@/components/Order";
import Register from "@/components/Register";

Vue.use(VueSession)
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
    {path: '/', component: Home},
    {path: '/product/:id', component: Product},
    {path: '/cart', component: Cart},
    {path: '/search', component: SearchResults},
    {path: '/login', component: Login},
    {path: '/profile', component: Profile},
    {path: '/pay', component: Payment},
    {path: '/order/:id', component: Order},
    {path: '/register', component: Register}
]

const router = new VueRouter(

    { // eslint-disable-next-line no-unused-vars
        routes, mode: 'history', scrollBehavior(to, from, savedPosition) {
            return {x: 0, y: 0, behavior: 'smooth'};
        }
    }
)

new Vue({
    render: h => h(App),
    router
}).$mount('#app')
