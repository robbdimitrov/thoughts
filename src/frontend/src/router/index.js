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
const ThoughtView = () => import('../views/ThoughtView.vue');
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
            { path: '/user/:location*', component: UserView },
            { path: '/settings', component: SettingsView,
                children: [
                    { path: 'account', component: ProfileView },
                    { path: 'password', component: PasswordView },
                    { path: '', redirect: 'account' }
                ]
            },
            { path: '/', redirect: '/feed' }
        ]
    });
}
