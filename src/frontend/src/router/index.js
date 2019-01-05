import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const FeedView = () => import('../views/FeedView.vue');
const ThoughtView = () => import('../views/ThoughtView.vue');
const UserView = () => import('../views/UserView.vue');

export function createRouter () {
    return new VueRouter({
        mode: 'history',
        routes: [
            { path: '/feed', component: FeedView },
            { path: '/thought', component: ThoughtView },
            { path: '/user', component: UserView },
            { path: '/', redirect: '/feed' }
        ]
    });
}
