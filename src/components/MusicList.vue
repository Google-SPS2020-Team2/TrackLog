<template>
  <div v-if="loading">
    <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
    <p>{{ message }}</p>
  </div>
  <div v-else-if="musics.length" id="music-list">
    <music-info v-for="music in musics"
                v-bind:key="music.id"
                v-bind:music="music"
    ></music-info>
  </div>
  <div v-else id="no-music">
    <p>There is no music to show.</p>
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
      message: 'Loading...',
      musics: []
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
            this.message = err;
          });
    }
  }
}
</script>

<style scoped>

</style>