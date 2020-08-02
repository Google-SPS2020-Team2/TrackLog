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
        <button class="md-button"
                v-on:click="$emit('delete', index)">
          <md-icon>delete</md-icon> &nbsp; <span>Delete</span>
        </button>
        <!--<button class="md-button">
          <md-icon>favorite</md-icon> &nbsp; <span>Favor</span>
        </button>-->
        <button class="md-button"
                v-if="!music.played"
                v-on:click="$emit('play', index)">
          <md-icon>play_circle_filled</md-icon> &nbsp; <span>Play</span>
        </button>
        <button class="md-button" v-else
                v-on:click="$emit('restore', index)">
          <md-icon>restore</md-icon> &nbsp; <span>Restore</span>
        </button>
      </md-card-actions>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "MusicInfo",
  props: ['index', 'music']
}
</script>

<style scoped>

</style>