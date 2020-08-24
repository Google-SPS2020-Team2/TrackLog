import Vue from 'vue';
import Router from 'vue-router';

import Welcome from '@/view/Welcome';
import MusicList from '@/view/MusicList';
import PlayedList from '@/view/PlayedList';
import UserInfo from '@/view/UserInfo';
import UserLogin from '@/view/UserLogin.vue';
import MusicDetail from '@/view/MusicDetail.vue';

import MainNavbar from "./layout/MainNavbar.vue";
import MainFooter from "./layout/MainFooter.vue";

import store from './store';

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/', 
      name: 'Welcome', 
      components: {default: Welcome, header: MainNavbar, footer: MainFooter},
      meta: {requiresAnonymous: true}
    },
    {
      path: '/login', 
      name: 'UserLogin', 
      components: {default: UserLogin, header: MainNavbar, footer: MainFooter},
      meta: {requiresAnonymous: true}
    },
    {
      path: '/music', 
      name: 'MusicList', 
      components: {default: MusicList, header: MainNavbar, footer: MainFooter},
      meta: {requiresLogin: true}
    },
    {
      path: '/played', 
      name: 'PlayedList', 
      components: {default: PlayedList, header: MainNavbar, footer: MainFooter},
      meta: {requiresLogin: true}
    },
    {
      path: '/user', 
      name: 'UserInfo', 
      component: UserInfo, 
      components: {default: UserInfo, header: MainNavbar, footer: MainFooter},
      meta: {requiresLogin: true},
      props: {
        header: { colorOnScroll: 200 },
        footer: { backgroundColor: "black" }
      }
    },
    {
      path: '/music/:id',
      name: 'MusicDetail',
      components: {default: MusicDetail, header: MainNavbar, footer: MainFooter},
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});

/**
 * Check whether the route requires user logged in before viewing.
 * If required and user has not logged in, redirect user to login.
 */
router.beforeResolve((to, from, next) => {
  const isLoggedIn = store.getters.userId !== null;
  if (to.matched.some(record => record.meta.requiresAnonymous) && isLoggedIn) {
    next("/music");
  }
  if (to.matched.some(record => record.meta.requiresLogin) && !isLoggedIn) {
    next("/login");
  }
  next();
});

export default router;
