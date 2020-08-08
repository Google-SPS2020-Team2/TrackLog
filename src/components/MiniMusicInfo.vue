<template>
  <div v-bind:id="'music-' + music.id " style="margin-bottom: 1rem;">
    <md-list-item to="/test" exact>
      <div class = "music-text">
        <span class="md-title" >{{ music.music_name }}</span>
        <p class = "md-info">Artist ID: {{ music.artist_id }} &amp; Difficulty: {{ music.difficulty }}</p>
      </div>
      <code>/</code>
    </md-list-item>
    <md-divider></md-divider>
  </div>
</template>

<script>
export default {
  name: "MiniMusicInfo",
  props: ['index', 'music']
}
</script>

<style scoped>
  .md-title {
    color: rgba(100,100,100,1);
  }
</style>