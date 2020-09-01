<template>
  <md-list>
    <md-list-item to="/music">
      <md-icon>queue_music</md-icon>
      <span class="md-list-item-text">Music</span>
    </md-list-item>
    <md-list-item to="/played">
      <md-icon>album</md-icon>
      <span class="md-list-item-text">Played</span>
    </md-list-item>
    <md-list-item to="/user">
      <md-icon>face</md-icon>
      <span class="md-list-item-text">User</span>
    </md-list-item>
  </md-list>
</template>

<script>
export default {
  name: 'AppDrawer'
}
</script>