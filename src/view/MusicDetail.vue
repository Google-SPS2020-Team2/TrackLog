<template>
  <div class="wrapper">
    <parallax
      class="section page-header header-filter"
      :style="headerStyle"
    >
      <div class="container">
        <div class="md-layout">
          <div class="md-layout-item">
            <h1 class="title text-center">Comments</h1>
            <h3 class="description text-center">
              Share your story
            </h3>
          </div>
        </div>
      </div>
    </parallax>
    <div class="main main-raised">
      <div class="section profile-content">
        <div class="container">
          <div class="comment_list">
            <h2 class = "comments text-center title">{{this.$route.params.name}}</h2>
            <md-divider></md-divider>
            <div v-if="comments.length" id="comment-list-data">
              <md-list>
                <comment-info v-for="(comment, index) in comments"
                            v-bind:key="index"
                            v-bind:index="index"
                            v-bind:comment="comment"
                            >
                </comment-info>
              </md-list>
            </div>
            <div v-else id="comment-list-empty">
              <p>There is no comment to show.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CommentInfo from "@/view/CommentInfo";
export default {
  name: "MusicDetail",
  components: {
    'comment-info': CommentInfo,
  },
  bodyClass: "list-page",
  data: function() {
    return {
      loading: true,
      loadingMessage: 'Loading...',
      comments: []
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
  },
  created: function() {
    this.getMusic();
  
  },
  methods: {
    getMusic() {
        this.$http.get('/getCommentAndScore', {
            params: {
                musicId:this.$route.params.id
            }
        })
            .then(res => {
                this.comments=res.data;
                this.loading = false;
            })
            .catch(err => {
                console.error(err);
            })
    }
  }
}
</script>

<style lang="scss" scoped>

.section {
  padding: 0;
}
</style>