// TOTO: user info with backend
// avatar.jpg is used for test, should be deleted later
<template>
  <div style="position: absolute;">
    <div class="info">
      <img class="avatar" :src="imgsrc">
      <p class = "nickname">nickname</p>
      <p class = "name">name</p>
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
      musics: []
    }
  },
  created: function () {
    this.getPlayedMusics();
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