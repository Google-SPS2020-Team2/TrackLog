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
              v-on:click="addMusicDialogActive = true">
        <md-icon>add_box</md-icon> &nbsp; <span>Add Music</span>
      </button>
    </h2>
    <div v-if="musics.length" id="music-list-data">
      <music-info v-for="(music, index) in musics"
                  v-bind:key="music.id"
                  v-bind:index="index"
                  v-bind:music="music"
                  v-on:delete="deleteMusic"
                  v-on:play="playMusic"
                  v-on:restore="restoreMusic">
      </music-info>
    </div>
    <div v-else id="music-list-empty">
      <p>There is no music to show.</p>
    </div>
    <md-dialog v-bind:md-active.sync="addMusicDialogActive">
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
        <button class="md-button" v-on:click="addMusicDialogActive = false">
          <md-icon>close</md-icon> &nbsp; <span>Cancel</span>
        </button>
        <button class="md-button" v-on:click="addMusic">
          <md-icon>check</md-icon> &nbsp; <span>Submit</span>
        </button>
      </md-dialog-actions>
    </md-dialog>
    <md-dialog-confirm
      md-title="Delete Music?"
      v-bind:md-content="'Are you sure you want to delete music ' + deleteMusicName + '?'"
      md-confirm-text="Yes"
      md-cancel-text="No"
      v-bind:md-active.sync="deleteMusicDialogActive"
      @md-cancel="deleteMusicDialogActive = false"
      @md-confirm="doDeleteMusic" />
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
      addMusicDialogActive: false,
      newMusic: {
        music_name: '',
        artist_id: 0,
        difficulty: ''
      },
      deleteMusicDialogActive: false,
      deleteMusicIndex: 0,
      deleteMusicName: ''
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
            this.addMusicDialogActive = false;
          })
          .catch(err => console.error(err));
    },
    deleteMusic(index) {
      /**
       * This method will open a dialog to confirm deletion,
       * the API request will be made in doDeleteMusic() method.
       */
      this.deleteMusicIndex = index;
      this.deleteMusicName = this.musics[index].music_name;
      this.deleteMusicDialogActive = true;
    },
    doDeleteMusic() {
      this.$http.post('/delete', {
        music_name: this.deleteMusicName
      })
          .then(() => {
            this.$delete(this.musics, this.deleteMusicIndex);
            this.deleteMusicDialogActive = false;
          })
          .catch(err => console.error(err));
    },
    playMusic(index) {
      this.$http.post('/add_practice', {
        music_id: this.musics[index].id,
        player_id: 0, // TODO: use real user ID
        score: 0,
        content: ''
      })
          .then(() => {
            this.$set(this.musics[index], 'played', true);
          })
          .catch(err => console.error(err));
    },
    restoreMusic(index) {
      this.$http.post('/delete_practice', {
        music_id: this.musics[index].id,
        player_id: 0, // TODO: use real user ID
      })
          .then(() => {
            this.$set(this.musics[index], 'played', false);
          })
          .catch(err => console.error(err));
    }
  }
}
</script>

<style scoped>

</style>