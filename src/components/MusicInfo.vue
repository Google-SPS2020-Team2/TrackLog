<template>
  <div v-bind:id="'music-' + music.id " style="margin-bottom: 1rem;">
    <md-card>
      <md-card-header>
        <span class="md-title">{{ music.music_name }}</span>
      </md-card-header>
      <md-card-content>
        <p>Artist ID: {{ music.artist_id }}</p>
        <p>Difficulty: {{ music.difficulty }}</p>
      </md-card-content>
      <md-card-actions>
        <button class="md-button">
          <md-icon>favorite</md-icon> &nbsp; <span>Favor</span>
        </button>
        <button class="md-button">
          <md-icon>play_circle_filled</md-icon> &nbsp; <span>Play</span>
        </button>
      </md-card-actions>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "MusicInfo",
  props: ['music']
}
</script>

<style scoped>

</style>