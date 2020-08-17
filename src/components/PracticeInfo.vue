<template>
  <div v-bind:id="'music-' + music.id " style="margin-bottom: 1rem;">
    <md-card class="practice-card">
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
          <p>score: {{music.score}}</p>
          <p v-if="music.content.length" class="content">"{{music.content}}"</p>
        </div>
      </md-card-content>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "PracticeInfo",
  props: ['simple', 'index', 'music'],
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

.content {
  font-size: 20px; 
  color: rgba(80,80,80,1);
}
.practice-card {
    width: 400px;
}

</style>