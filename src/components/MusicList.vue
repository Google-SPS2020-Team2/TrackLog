<template>
  <div v-if="loading" id="music-list-loading">
    <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
    <p>{{ loadingMessage }}</p>
  </div>
  <div v-else id="music-list-loaded">
    <h2 style="margin-bottom: 2rem;">
      Music List
      <button class="md-button"
              style="float: right; margin-top: 0;"
              @click="showAddMusicDialog = true">
        <md-icon>add_box</md-icon> &nbsp; <span>Add Music</span>
      </button>
    </h2>
    <div v-if="musics.length" id="music-list-data">
      <music-info v-for="music in musics"
                  v-bind:key="music.id"
                  v-bind:music="music"
                  v-on:delete="deleteMusic"
      ></music-info>
    </div>
    <div v-else id="music-list-empty">
      <p>There is no music to show.</p>
    </div>
    <md-dialog v-bind:md-active.sync="showAddMusicDialog">
      <md-dialog-title>Add Music</md-dialog-title>
      <md-dialog-content>
        <form novalidate class="md-layout">
          <md-field>
            <label for="dialog-music-name">Music Name</label>
            <md-input name="dialog-music-name" id="dialog-music-name" v-model="newMusic.music_name"/>
          </md-field>
          <md-field>
            <label for="dialog-artist-id">Artist ID</label>
            <md-input name="dialog-artist-id" id="dialog-artist-id" type="number" v-model="newMusic.artist_id"/>
          </md-field>
          <md-field>
            <label for="dialog-difficulty">Difficulty</label>
            <md-input name="dialog-difficulty" id="dialog-difficulty" v-model="newMusic.difficulty"/>
          </md-field>
        </form>
      </md-dialog-content>
      <md-dialog-actions style="margin: 1rem;">
        <button class="md-button" @click="showAddMusicDialog = false">
          <md-icon>close</md-icon> &nbsp; <span>Cancel</span>
        </button>
        <button class="md-button" @click="addMusic">
          <md-icon>check</md-icon> &nbsp; <span>Submit</span>
        </button>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>

<script>
import MusicInfo from "@/components/MusicInfo";

export default {
  name: "MusicList",
  components: {
    'music-info': MusicInfo
  },
  data: function () {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      musics: [],
      showAddMusicDialog: false,
      newMusic: {
        music_name: '',
        artist_id: 0,
        difficulty: ''
      }
    }
  },
  created: function () {
    this.getMusics();
  },
  methods: {
    getMusics() {
      this.$http.get('/show')
          .then(res => {
            this.musics = res.data;
            this.loading = false;
          })
          .catch(err => {
            console.error(err);
            this.loadingMessage = err;
          });
    },
    addMusic() {
      this.$http.post('/add', this.newMusic)
          .then(() => {
            this.getMusics();
            this.showAddMusicDialog = false;
          })
          .catch(err => console.error(err));
    },
    deleteMusic(musicId) {
      let index = -1;
      for (index = 0; index < this.musics.length; ++index) {
        if (this.musics[index].music_id === musicId) break;
      }
      if (index >= this.musics.length) return;

      this.$http.post('/delete', {
        music_name: this.musics[index].music_name
      })
          .then(() => {
            this.$delete(this.musics, index);
          })
          .catch(err => console.error(err));
    }
  }
}
</script>

<style scoped>

</style>