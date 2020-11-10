import Vue from 'vue'
import VueRouter from 'vue-router'
import Product from './views/Product.vue'
import Cart from './views/Cart.vue'

//DO THE SAME FOR CART

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'product',
            component: Product
        },
        {
            path: '/',
            name: 'cart',
            component: Cart
        }
    ]
})