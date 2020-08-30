<template>
  <div class="wrapper">
    <parallax
        class="section page-header header-filter"
        :style="headerStyle"
    >
      <div class="container">
        <div class="md-layout">
          <div class="md-layout-item">
            <h1 class="title text-center">Music</h1>
            <h4 class="description text-center">
              Look for your track here.
            </h4>
          </div>
        </div>
      </div>
    </parallax>
    <div class="main main-raised">
      <div class="section profile-content">
        <div class="container">
          <div v-if="loading" id="music-list-loading">
            <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
            <p>{{ loadingMessage }}</p>
          </div>
          <div class="music_list" v-else id="music-list-loaded">
            <div id="music-search-input">
              <md-field>
                <md-icon>search</md-icon>
                <label>Search Music</label>
                <md-input v-model="keyword" v-on:keyup.enter="getMusics(1)"></md-input>
              </md-field>
            </div>
            <md-button class="md-success md-round md-just-icon"
                       style="float: right; margin-top: 0;"
                       v-on:click="addMusicDialogActive = true">
              <md-icon>add</md-icon>
            </md-button>
            <div v-if="musics.length" id="music-list-data">
              <md-list>
                <music-info v-for="(music, index) in musics"
                            v-bind:key="music.id"
                            v-bind:simple="false"
                            v-bind:index="index"
                            v-bind:music="music"
                            v-on:delete="deleteMusic(index)"
                            v-on:addPractice="addPracticeOfMusic(index)"
                            v-on:deletePractice="deletePracticeOfMusic(index)">
                </music-info>
              </md-list>
              <div id="musics-pagination" style="text-align: center;">
                <md-button style="float: left;"
                           v-bind:disabled="pageIndex <= 1"
                           v-on:click="showPrevPage()">
                  Previous Page
                </md-button>
                <md-button disabled>{{ (pageIndex - 1) * pageSize + 1 }} - {{ pageIndex * pageSize }} of {{
                    totalItems
                  }}
                </md-button>
                <md-button style="float: right;"
                           v-bind:disabled="pageIndex >= totalPages"
                           v-on:click="showNextPage()">
                  Next Page
                </md-button>
              </div>
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
                    <md-input name="dialog-practice-score" id="dialog-practice-score" type="number"
                              v-model="newPractice.score"/>
                  </md-field>
                  <md-field>
                    <label for="dialog-practice-content">Content</label>
                    <md-textarea md-autogrow name="dialog-practice-content" id="dialog-practice-content"
                                 v-model="newPractice.content"/>
                  </md-field>
                </form>
              </md-dialog-content>
              <md-dialog-actions style="margin: 1rem;">
                <md-button class="md-primary" v-on:click="addPracticeDialogActive = false">
                  <md-icon>close</md-icon>Cancel
                </md-button>
                <md-button class="md-primary" v-on:click="doAddPracticeOfMusic">
                  <md-icon>check</md-icon>Submit
                </md-button>
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
                        <md-select name="dialog-artist" id="dialog-artist" v-model="newMusic.artist_id">
                          <md-option
                              v-for="(artist, index) in artists"
                              v-bind:key="artist.id"
                              v-bind:index="index"
                              v-bind:artist="artist"
                              :value=parseInt(artist.id)>
                            {{ artist.artist_name }}
                          </md-option>
                        </md-select>
                      </md-field>
                    </div>
                    <md-button class="md-primary" style="margin: 1rem;" v-on:click="addArtistDialogActive = true">add
                      artist
                    </md-button>
                  </div>
                  <!-- <md-field>
                    <label for="dialog-difficulty">Difficulty</label>
                    <md-input name="dialog-difficulty" id="dialog-difficulty" v-model="newMusic.difficulty"/>
                  </md-field> -->
                </form>
              </md-dialog-content>
              <md-dialog-actions style="margin: 1rem;">
                <md-button class="md-button md-success" v-on:click="addMusicDialogActive = false">
                  <md-icon>close</md-icon>
                  Cancel
                </md-button>
                <md-button class="md-button md-success" v-on:click="addMusic">
                  <md-icon>check</md-icon>
                  Submit
                </md-button>
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
                <md-button class="md-button md-success" v-on:click="addArtistDialogActive = false">
                  <md-icon>close</md-icon>
                  Cancel
                </md-button>
                <md-button class="md-button md-success" v-on:click="addArtist">
                  <md-icon>check</md-icon>
                  Submit
                </md-button>
              </md-dialog-actions>
            </md-dialog>

            <md-dialog-confirm
                md-title="Delete Music?"
                v-bind:md-content="'Are you sure you want to delete music ' + deleteMusicName + '?'"
                md-confirm-text="Yes"
                md-cancel-text="No"
                v-bind:md-active.sync="deleteMusicDialogActive"
                @md-cancel="deleteMusicDialogActive = false"
                @md-confirm="doDeleteMusic"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MusicInfo from "@/view/MusicInfo";

export default {
  name: "MusicList",
  components: {
    'music-info': MusicInfo,
  },
  bodyClass: "list-page",
  data: function () {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      keyword: this.$route.query.keyword || '',
      pageSize: 0,
      totalItems: 0,
      totalPages: 1,
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
        // difficulty: ''
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
  props: {
    header: {
      type: String,
      default: require("@/assets/img/city-profile.jpg")
    },
    img: {
      type: String,
      default: require("@/assets/img/faces/christian.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    },
    pageIndex() {
      return Number(this.$route.query.page) || 1;
    },
  },
  created: function () {
    this.getMusics(this.pageIndex);
    this.getArtists();
  },
  watch: {
    pageIndex() {
      this.getMusics();
    }
  },
  methods: {
    getMusics(page = null) {
      let promise = null;
      if (this.keyword) {
        const query = {keyword: this.keyword, page: page ? page : this.pageIndex.toString()};
        this.$router.push({path: '/music', query: query});
        promise = this.$http.get('/searchMusic', {
          params: {
            musicName: this.keyword,
            page: this.pageIndex
          }
        });
      } else {
        promise = this.$http.get('/show', {
          params: {
            page: this.pageIndex
          }
        });
      }
      promise // execute to load musics
          .then(res => {
            this.musics = res.data.items;
            this.pageSize = res.data.pageSize;
            this.totalItems = res.data.totalItems;
            this.totalPages = res.data.totalPages;
            this.loading = false;
          })
          .catch(err => {
            console.error(err);
            this.loadingMessage = err;
          });
    },
    showPrevPage() {
      const query = {};
      if (this.keyword) {
        query.keyword = this.keyword;
      }
      query.page = (this.pageIndex - 1).toString();
      this.$router.push({path: '/music', query: query});
    },
    showNextPage() {
      const query = {};
      if (this.keyword) {
        query.keyword = this.keyword;
      }
      query.page = (this.pageIndex + 1).toString();
      this.$router.push({path: '/music', query: query});
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
            this.artists = res.data.items;
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

<style lang="scss" scoped>

.section {
  padding: 0;
}
</style>