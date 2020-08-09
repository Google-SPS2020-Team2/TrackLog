<template>
  <md-list>
    <md-list-item to="/" exact>
      <md-icon>home</md-icon>
      <span class="md-list-item-text">Home</span>
    </md-list-item>
    <md-list-item to="/login" v-if="!userLoggedIn">
      <md-icon>login</md-icon>
      <span class="md-list-item-text">Login</span>
    </md-list-item>
    <md-list-item to="/music" v-if="userLoggedIn">
      <md-icon>queue_music</md-icon>
      <span class="md-list-item-text">Music</span>
    </md-list-item>
    <md-list-item to="/played" v-if="userLoggedIn">
      <md-icon>album</md-icon>
      <span class="md-list-item-text">Played</span>
    </md-list-item>
    <md-list-item to="/user" v-if="userLoggedIn">
      <md-icon>face</md-icon>
      <span class="md-list-item-text">User</span>
    </md-list-item>
  </md-list>
</template>

<script>
export default {
  name: 'AppDrawer',
  computed: {
    userLoggedIn() {
      return this.$store.getters.userId !== null;
    }
  }
}
</script>