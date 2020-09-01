<template>
  <div class="wrapper">
    <parallax
      class="section page-header header-filter"
      :style="headerStyle"
    ></parallax>
    <div class="main main-raised">
      <div class="section profile-content">
        <div class="container">
          <div class="md-layout">
            <div class="md-layout-item md-size-50 mx-auto">
              <div class="profile">
                <div class="avatar">
                  <img
                    :src="img"
                    alt="Circle Image"
                    class="img-raised rounded-circle img-fluid"
                  />
                </div>
                <div class="name">
                  <h3 class="title">{{username}}</h3>
                  <h6>{{nickname}}</h6>
                </div>
              </div>
            </div>
          </div>
          <div class="description text-center">
            <p>
              (maybe user can add info here) An artist of considerable range, Chet Faker — the name taken by
              Melbourne-raised, Brooklyn-based Nick Murphy — writes, performs
              and records all of his own music, giving it a warm, intimate feel
              with a solid groove structure.
            </p>
            <md-button class="md-primary"
                      v-on:click="logout()">
              Logout
            </md-button>
          </div>

          <div class="music_list">
            <h2 class = "played-music text-center title">Played Music list</h2>
            <md-divider></md-divider>
            <div v-if="musics.length" id="music-list-data">
              <md-list>
                <music-info v-for="(music, index) in musics"
                          v-bind:key="music.id"
                          v-bind:index="index"
                          v-bind:music="music">
                </music-info>
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
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { Tabs } from "@/components";
import MiniMusicInfo from "@/view/MiniMusicInfo";
export default {
  name: "UserInfo",
  components: {
    'music-info': MiniMusicInfo,
    // Tabs
  },
  bodyClass: "profile-page",
  data: function() {
    return {
      musics: [],
      username: " ",
      nickname: " ",
      pageSize: 0,
      totalItems: 0,
      totalPages: 0
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
    this.getUserInfo();
  },
  watch: {
    pageIndex() {
      this.getPlayedMusics();
    }
  },
  methods: {
    logout() {
      this.$http.get('/logout')
        .then(() => {
          this.$store.commit('userLogout');
          this.$router.push('/login');
        });
    },
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
          });
    },
    showPrevPage() {
      this.$router.push({path: '/user', query: {page: (this.pageIndex - 1).toString()}});
    },
    showNextPage() {
      this.$router.push({path: '/user', query: {page: (this.pageIndex + 1).toString()}});
    },
    getUserInfo() {
      this.$http.get('/status')
          .then(res => {
            this.username = res.data.username;
            this.nickname = res.data.nickname;
          });
    }
  }
}
</script>

<style lang="scss" scoped>

.section {
  padding: 0;
}

.profile-tabs::v-deep {
  .md-card-tabs .md-list {
    justify-content: center;
  }

  [class*="tab-pane-"] {
    margin-top: 3.213rem;
    padding-bottom: 50px;

    img {
      margin-bottom: 2.142rem;
    }
  }
}
</style>