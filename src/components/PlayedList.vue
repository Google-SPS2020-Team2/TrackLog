<template>
  <div v-if="loading" id="music-list-loading">
    <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
    <p>{{ loadingMessage }}</p>
  </div>
  <div v-else id="music-list-loaded">
    <h2 style="margin-bottom: 2rem;">
      Played Music List
    </h2>
    <div v-if="musics.length" id="music-list-data">
      <music-info v-for="(music, index) in musics"
                  v-bind:key="music.id"
                  v-bind:simple="true"
                  v-bind:index="index"
                  v-bind:music="music">
      </music-info>
    </div>
    <div v-else id="music-list-empty">
      <p>There is no music to show.</p>
    </div>
  </div>
</template>

<script>
import MusicInfo from "@/components/MusicInfo";

export default {
  name: "PlayedList",
  components: {
    'music-info': MusicInfo
  },
  data: function () {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      musics: []
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