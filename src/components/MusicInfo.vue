<template>
  <div v-bind:id="'music-' + music.id " style="margin-bottom: 1rem;">
    <md-card>
      <md-card-header>
        <span class="md-title">{{ music.music_name }}</span>
      </md-card-header>
      <md-card-content>
        <div v-if="artist === null">
          Loading artist info...
        </div>
        <div v-else>
          <p>Artist: {{ artist.artist_name }}</p>
          <p>Difficulty: {{ music.difficulty }}</p>
        </div>
      </md-card-content>
      <md-card-actions>
        <button class="md-button"
                v-on:click="$emit('delete', index)">
          <md-icon>delete</md-icon> &nbsp; <span>Delete</span>
        </button>
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
  props: ['index', 'music'],
  data: function() {
    return {
      artist: null
    }
  },
  created: function() {
    this.getArtist();
  },
  methods: {
    getArtist() {
      this.$http.get('/get_artist_info', {
        params: {
          id: this.music.artist_id
        }
      }).then(res => {
        this.artist = res.data[0];
      }).catch(err => {
        console.error(err);
      })
    }
  }
}
</script>

<style scoped>

</style>