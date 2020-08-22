<template>
  <div v-if="loading" id="music-list-loading">
    <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
    <p>{{ loadingMessage }}</p>
  </div>
  <div v-else id="music-list-loaded">
    <h2 style="margin-bottom: 2rem;">
      Played Music List
    </h2>
    <div id="music-search-input">
      <md-field>
        <md-icon>search</md-icon>
        <label>Search Music</label>
        <md-input v-model="keyword"></md-input>
      </md-field>
    </div>
    <div class="md-layout md-gutter" :class="`md-alignment-top`" v-if="musics.length" id="music-list-data">
      <practice-info v-for="(music, index) in filteredMusics"
                  v-bind:key="music.id"
                  v-bind:simple="true"
                  v-bind:index="index"
                  v-bind:music="music">
      </practice-info>
    </div>
    <div v-else id="music-list-empty">
      <p>There is no music to show.</p>
    </div>
  </div>
</template>

<script>
import PracticeInfo from "@/components/PracticeInfo";

export default {
  name: "PlayedList",
  components: {
    'practice-info': PracticeInfo
  },
  data: function () {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      keyword: '',
      musics: []
    }
  },
  computed: {
    filteredMusics() {
      if (this.keyword) {
        return this.musics.filter(m => m.music_name.indexOf(this.keyword) >= 0);
      } else {
        // No keyword given, return all musics.
        return this.musics;
      }
    }
  },
  created: function () {
    this.getPlayedMusics();
  },
  methods: {
    getPlayedMusics() {
      this.$http.get('/show_practice')
          .then(res => {
            this.musics = res.data;
            this.loading = false;
          })
          .catch(err => {
            console.error(err);
            this.loadingMessage = err;
          });
    }
  }
}
</script>

<style scoped>

</style>