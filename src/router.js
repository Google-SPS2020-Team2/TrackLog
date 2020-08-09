import Vue from 'vue';
import Router from 'vue-router';

import AppHome from '@/components/AppHome';
import MusicList from '@/components/MusicList';
import PlayedList from '@/components/PlayedList';
import UserInfo from '@/components/UserInfo';
import UserLogin from '@/components/UserLogin.vue';

import store from './store';

Vue.use(Router);

const router = new Router({
  routes: [
    {path: '/', name: 'Home', component: AppHome},
    {path: '/login', name: 'UserLogin', component: UserLogin},
    {path: '/music', name: 'MusicList', component: MusicList, meta: {requiresLogin: true}},
    {path: '/played', name: 'PlayedList', component: PlayedList, meta: {requiresLogin: true}},
    {path: '/user', name: 'UserInfo', component: UserInfo, meta: {requiresLogin: true}}
  ]
});

/**
 * Check whether the route requires user logged in before viewing.
 * If required and user has not logged in, redirect user to login.
 */
router.beforeResolve((to, from, next) => {
  const isLoggedIn = store.getters.userId !== null;
  if (to.matched.some(record => record.meta.requiresLogin) && !isLoggedIn) {
    next("/login");
  }
  next();
});

export default router;