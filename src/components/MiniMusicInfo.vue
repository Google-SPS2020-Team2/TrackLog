<template>
  <div v-bind:id="'music-' + music.id " style="margin-bottom: 1rem;">
    <md-list-item to="/test" exact>
      <div class = "music-text">
        <span class="md-title" >{{ music.music_name }}</span>
        <p class="md-info" v-if="artist === null">
          Loading artist info...
        </p>
        <p class="md-info" v-else>
          Artist: {{ artist.artist_name }} &amp; Difficulty: {{ music.difficulty }}
        </p>
      </div>
      <code>/</code>
    </md-list-item>
    <md-divider></md-divider>
  </div>
</template>

<script>
export default {
  name: "MiniMusicInfo",
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
      })
          .then(res => {
            this.artist = res.data[0];
          })
          .catch(err => {
            console.error(err);
          })
    }
  }
}
</script>

<style scoped>
  .md-title {
    color: rgba(100,100,100,1);
  }
</style>