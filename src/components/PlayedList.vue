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
      <div id="musics-pagination" style="text-align: center;">
        <md-button style="float: left;"
                   v-bind:disabled="pageIndex <= 1"
                   v-on:click="showPrevPage()">
          Previous Page
        </md-button>
        <md-button disabled>{{ (pageIndex - 1) * pageSize + 1 }} - {{ pageIndex * pageSize }} of {{ totalItems }}</md-button>
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
      pageSize: 0,
      totalItems: 0,
      totalPages: 0,
      musics: []
    }
  },
  computed: {
    pageIndex() {
      return Number(this.$route.query.page) || 1;
    },
    filteredMusics() {
      if (this.keyword) {
        const keywordToLowerCase = this.keyword.toLowerCase();
        return this.musics.filter(m => m.music_name.toLowerCase().indexOf(keywordToLowerCase) >= 0);
      } else {
        // No keyword given, return all musics.
        return this.musics;
      }
    }
  },
  watch: {
    pageIndex() {
      this.getPlayedMusics();
    }
  },
  created: function () {
    this.getPlayedMusics();
  },
  methods: {
    getPlayedMusics() {
      this.$http.get('/show_practice', {
        params: {
          page: this.pageIndex
        }
      })
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
      this.$router.push({path: '/played', query: {page: (this.pageIndex - 1).toString()}});
    },
    showNextPage() {
      this.$router.push({path: '/played', query: {page: (this.pageIndex + 1).toString()}});
    },
  }
}
</script>

<style scoped>

</style>