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
                  v-bind:simple="false"
                  v-bind:index="index"
                  v-bind:music="music"
                  v-on:delete="deleteMusic(index)"
                  v-on:addPractice="addPracticeOfMusic(index)"
                  v-on:deletePractice="deletePracticeOfMusic(index)">
      </music-info>
    </div>
    <div v-else id="music-list-empty">
      <p>There is no music to show.</p>
    </div>
    <md-dialog v-bind:md-active.sync="addPracticeDialogActive">
      <md-dialog-title>Add Practice for {{ addPracticeMusicName }}</md-dialog-title>
      <md-dialog-content>
        <form novalidate class="md-layout">
          <md-field>
            <label for="dialog-practice-score">Score</label>
            <md-input name="dialog-practice-score" id="dialog-practice-score" type="number" v-model="newPractice.score"/>
          </md-field>
          <md-field>
            <label for="dialog-practice-content">Content</label>
            <md-textarea md-autogrow name="dialog-practice-content" id="dialog-practice-content" v-model="newPractice.content"/>
          </md-field>
        </form>
      </md-dialog-content>
      <md-dialog-actions style="margin: 1rem;">
        <button class="md-button" v-on:click="addPracticeDialogActive = false">
          <md-icon>close</md-icon> &nbsp; <span>Cancel</span>
        </button>
        <button class="md-button" v-on:click="doAddPracticeOfMusic">
          <md-icon>check</md-icon> &nbsp; <span>Submit</span>
        </button>
      </md-dialog-actions>
    </md-dialog>

    <md-dialog v-bind:md-active.sync="addMusicDialogActive">
      <md-dialog-title>Add Music</md-dialog-title>
      <md-dialog-content>
        <form novalidate class="md-layout">
          <md-field>
            <label for="dialog-music-name">Music Name</label>
            <md-input name="dialog-music-name" id="dialog-music-name" v-model="newMusic.music_name"/>
          </md-field>
          <div class="md-layout md-gutter"> 
            <div class="md-layout-item">
              <md-field>
                <label for="dialog-artist">Artist</label>
                <md-select name="dialog-artist" id="dialog-artist"  v-model="newMusic.artist_id">
                  <md-option
                    v-for="(artist, index) in artists"
                    v-bind:key="artist.id"
                    v-bind:index="index"
                    v-bind:artist="artist"
                    :value=parseInt(artist.id)>
                    {{artist.artist_name}}
                  </md-option>
                </md-select>
              </md-field>
            </div>
            <md-button style="margin: 1rem;" v-on:click="addArtistDialogActive = true">add artist</md-button>
          </div>
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

    <md-dialog v-bind:md-active.sync="addArtistDialogActive">
      <md-dialog-title>Add Artist</md-dialog-title>
      <md-dialog-content>
        <form>
          <md-field>
            <label for="dialog-artist-name">Artist Name</label>
            <md-input name="dialog-artist-name" id="dialog-artist-name" v-model="newArtist.name"/>
          </md-field>
          <md-field>
            <label for="dialog-introduction">Introduction</label>
            <md-input name="dialog-introduction" id="dialog-introduction" v-model="newArtist.introduction"/>
          </md-field>
        </form>
      </md-dialog-content>
      <md-dialog-actions style="margin: 1rem;">
        <button class="md-button" v-on:click="addArtistDialogActive = false">
          <md-icon>close</md-icon> &nbsp; <span>Cancel</span>
        </button>
        <button class="md-button" v-on:click="addArtist">
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
    'music-info': MusicInfo,
  },
  data: function () {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      musics: [],
      artists: [],
      addPracticeDialogActive: false,
      addPracticeMusicIndex: 0,
      addPracticeMusicName: '',
      newPractice: {
        score: 0,
        content: ''
      },
      addMusicDialogActive: false,
      newMusic: {
        music_name: '',
        artist_id: 0,
        difficulty: ''
      },
      addArtistDialogActive: false,
      newArtist: {
        name: '',
        introduction: ''
      },
      deleteMusicDialogActive: false,
      deleteMusicIndex: 0,
      deleteMusicName: ''
    }
  },
  created: function () {
    this.getMusics();
    this.getArtists();
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
    addPracticeOfMusic(index) {
      /**
       * This method will open a dialog to let user input score and content,
       * the API request will be made in doAddPracticeOfMusic() method.
       */
      this.addPracticeDialogActive = true;
      this.addPracticeMusicIndex = index;
      this.addPracticeMusicName = this.musics[index].music_name;
    },
    doAddPracticeOfMusic() {
      this.$http.post('/add_practice', {
        music_id: this.musics[this.addPracticeMusicIndex].id,
        score: this.newPractice.score,
        content: this.newPractice.content
      })
          .then(() => {
            this.addPracticeDialogActive = false;
            this.$set(this.musics[this.addPracticeMusicIndex], 'played', true);
          })
          .catch(err => console.error(err));
    },
    deletePracticeOfMusic(index) {
      this.$http.post('/delete_practice', {
        music_id: this.musics[index].id,
      })
          .then(() => {
            this.$set(this.musics[index], 'played', false);
          })
          .catch(err => console.error(err));
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
    getArtists() {
      this.$http.get('/show_artist')
          .then(res => {
            this.artists = res.data;
          })
          .catch(err => console.error(err));
    },
    addArtist() {
      this.$http.post('/add_artist', this.newArtist)
          .then(() => {
            this.getArtists();
            this.addArtistDialogActive = false;
          })
          .catch(err => console.error(err));
    }
  }
}
</script>

<style scoped>

</style>