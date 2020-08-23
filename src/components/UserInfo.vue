// TOTO: user info with backend
// avatar.jpg is used for test, should be deleted later
<template>
  <div style="position: absolute;">
    <div class="info">
      <img class="avatar" :src="imgsrc">
      <p class = "nickname">{{nickname}}</p>
      <p class = "name">{{username}}</p>
      <md-button class="md-accent" style="width: 95%;"
                 v-on:click="logout()">
        Logout
      </md-button>
    </div>
    <div class="music_list">
      <h2 style = "color: rgba(80,80,80,1);">Played Music list</h2>
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
</template>

<script>
import avatar from "@/assets/avatar.jpg";
import MiniMusicInfo from "@/components/MiniMusicInfo";

export default {
  name: "UserInfo",
  components: {
    'music-info': MiniMusicInfo
  },
  data: function() {
    return {
      imgsrc:avatar,
      pageSize: 0,
      totalItems: 0,
      totalPages: 0,
      musics: [],
      username: " ",
      nickname: " "
    }
  },
  computed: {
    pageIndex() {
      return Number(this.$route.query.page) || 1;
    }
  },
  watch: {
    pageIndex() {
      this.getPlayedMusics();
    }
  },
  created: function () {
    this.getPlayedMusics();
    this.getUserInfo();
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

<style scoped>
  .info {
    margin-top: 2rem; 
    margin-left: 50px; 
    width:200px;
  }
  .avatar {
    width:200px; 
    height:200px; 
    border-radius: 50%;
  }
  .nickname {
    font-size: 20px; 
    font-weight: bold; 
    margin-top: 1rem;
  }
  .name {
    font-size: 15px; 
    margin-top: -1.1rem; 
  }
  .music_list {
    position: absolute; 
    left: 320px; top: 0px; right: 0px; 
    width:1000px;
  }
  .md-list {
    width: 1000px;
    max-width: 100%;
    display: inline-block;
    vertical-align: top;
    border: 1px solid rgba(#000, .12);
  }
</style>