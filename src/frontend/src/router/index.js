import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const FeedView = () => import('../views/FeedView.vue');
const ThoughtView = () => import('../views/ThoughtView.vue');
const UserView = () => import('../views/UserView.vue');
const ThoughtList = () => import('../components/ThoughtList.vue');
const UserList = () => import('../components/UserList.vue');

export function createRouter () {
    return new VueRouter({
        mode: 'history',
        routes: [
            { path: '/feed', component: FeedView },
            { path: '/thought', component: ThoughtView },
            { path: '/user', component: UserView,
            children: [
                { path: 'thoughts', component: ThoughtList },
                { path: 'following', component: UserList },
                { path: 'followers', component: UserList },
                { path: 'likes', component: ThoughtList },
                { path: '/user', redirect: '/user/thoughts' }
              ]
            },
            { path: '/', redirect: '/feed' }
        ]
    });
}
