<template>
  <div class="wrapper">
    <parallax
      class="section page-header header-filter"
      :style="headerStyle"
    >
      <div class="container">
        <div class="md-layout">
          <div class="md-layout-item">
            <h1 class="title text-center">Played</h1>
            <h4 class="description text-center">
              What you have played in the past..
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
            <div v-if="musics.length" id="music-list-data">
              <md-list>
                <practice-info v-for="(music, index) in musics"
                            v-bind:key="music.id"
                            v-bind:simple="false"
                            v-bind:index="index"
                            v-bind:music="music">
                </practice-info>
              </md-list>
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
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PracticeInfo from "@/view/PracticeInfo";
export default {
  name: "PlayedList",
  components: {
    'practice-info': PracticeInfo
  },
  bodyClass: "list-page",
  data: function() {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      pageSize: 0,
      totalItems: 0,
      totalPages: 1,
      musics: []
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
      this.$router.push({path: '/music', query: {page: (this.pageIndex - 1).toString()}});
    },
    showNextPage() {
      this.$router.push({path: '/music', query: {page: (this.pageIndex + 1).toString()}});
    }
  }
}
</script>

<style lang="scss" scoped>

.section {
  padding: 0;
}
</style>