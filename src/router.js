import Vue from 'vue';
import Router from 'vue-router';

import AppHome from '@/components/AppHome';
import MusicList from '@/components/MusicList';
import PlayedList from '@/components/PlayedList';
import UserInfo from '@/components/UserInfo';

Vue.use(Router);

export default new Router({
  routes: [
    {path: '/', name: 'Home', component: AppHome},
    {path: '/music', name: 'MusicList', component: MusicList},
    {path: '/played', name: 'PlayedList', component: PlayedList},
    {path: '/user', name: 'UserInfo', component: UserInfo}
  ]
});
