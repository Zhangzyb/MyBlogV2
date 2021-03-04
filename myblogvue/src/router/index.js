import VueRouter from 'vue-router'
import Vue from 'vue'

const Home = () => import('views/home/Home')
const Category = () => import('views/category/Category')
const TimeLine = () => import('views/timeline/TimeLine')
const Dynamic = () => import('views/dynamic/Dynamic')

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/category',
        component: Category
    },
    {
        path: '/timeline',
        component: TimeLine
    },
    {
        path: '/dynamic',
        component: Dynamic
    }
]

const router = new VueRouter({
    routes,
    mode: 'history'
})

export default router