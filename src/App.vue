<template>
  <div id="app">
    <md-app style="min-height: 100vh;">
      <md-app-toolbar class="md-primary">
        <span class="md-title">TrackLog</span>
      </md-app-toolbar>
      <md-app-drawer md-permanent="full">
        <md-toolbar class="md-transparent" md-elevation="0">
          <md-icon>library_music</md-icon>
        </md-toolbar>
        <app-drawer></app-drawer>
      </md-app-drawer>
      <md-app-content>
        <router-view></router-view>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>
import AppDrawer from "@/components/AppDrawer";
export default {
  name: 'App',
  components: {
    'app-drawer': AppDrawer
  }
}
</script>

<style>
.md-drawer {
  width: unset !important;
}
</style>
