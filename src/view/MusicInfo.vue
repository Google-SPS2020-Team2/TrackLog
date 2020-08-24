<template>
  <div v-bind:id="'music-' + music.id " style="margin-bottom: 1rem;">
    <md-card md-with-hover>
      <!-- <md-card-header>
        <span class="md-title">{{ music.music_name }}</span>
      </md-card-header> -->
      <md-card-content>
        <div class="card-header">
          <h3>{{ music.music_name }}</h3>
        </div>
        <div v-if="artist === null">
          Loading artist info...
        </div>
        <div v-else>
          <p>Artist: {{ artist.artist_name }}</p>
          <p>Difficulty: {{ music.difficulty }}</p>
        </div>
      </md-card-content>
      <md-card-actions v-if="!simple">
        <md-button class="button md-success md-round" v-on:click="to">
          Comments..
        </md-button>
        <md-button class="button md-success md-round"
                v-on:click="$emit('delete', index)">
          <md-icon >delete</md-icon> Delete
        </md-button>
        <md-button class="button md-success md-round"
                v-if="!music.played"
                v-on:click="$emit('addPractice', index)">
          <md-icon>play_circle_filled</md-icon>Add Practice
        </md-button>
        <md-button class="button md-success md-round" v-else
                v-on:click="$emit('deletePractice', index)">
          <md-icon>restore</md-icon>Delete Practice
        </md-button>
      </md-card-actions>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "MusicInfo",
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
    to() {
      this.$router.push({
        name:'MusicDetail',
        params: {
          id: this.music.id,
          name: this.music.music_name
        }
      })
    },
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
.button {
    margin: 0 2px 15px;
}
</style>