import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const FeedView = () => import('../views/FeedView.vue');
const LoginView = () => import('../views/LoginView.vue');
const PasswordView = () => import('../views/PasswordView.vue');
const ProfileView = () => import('../views/ProfileView.vue');
const SearchView = () => import('../views/SearchView.vue');
const SettingsView = () => import('../views/SettingsView.vue');
const SignupView = () => import('../views/SignupView.vue');
const ThoughtList = () => import('../components/ThoughtList.vue');
const ThoughtView = () => import('../views/ThoughtView.vue');
const UserList = () => import('../components/UserList.vue');
const UserView = () => import('../views/UserView.vue');

export function createRouter () {
    return new VueRouter({
        mode: 'history',
        routes: [
            { path: '/feed', component: FeedView },
            { path: '/login', component: LoginView },
            { path: '/signup', component: SignupView },
            { path: '/search', component: SearchView },
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
            { path: '/settings', component: SettingsView },
            { path: '/settings/password', component: PasswordView },
            { path: '/settings/account', component: ProfileView },
            { path: '/', redirect: '/feed' }
        ]
    });
}
