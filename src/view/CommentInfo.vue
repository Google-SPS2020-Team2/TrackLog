<template>
  <div v-bind:id="'comment-' + comment.id " style="margin-bottom: 1rem;">
    <md-list-item>
      <div class = "comment-text">
        <h5 class="md-title" >{{ comment.nickname }}: score {{comment.score}}</h5>
        <span class="md-title begin">
          comment: 
        </span>
        <span class="md-info">
          {{ comment.content }}
        </span>
      </div>
    </md-list-item>
    <md-divider></md-divider>
  </div>
</template>

<script>
export default {
  name: "CommentInfo",
  props: ['index', 'comment']
}
</script>

<style scoped>
  .md-title {
    color: rgba(100,100,100,1);
  }
  .begin {
    font-size:1.2rem;
    color: rgba(100,100,100,1);
  }
  .md-info{
    font-size:1.1rem;
    color: rgb(112, 112, 112);
    text-shadow: 0px 15px 102.86px rgba(0, 0, 0, 0.7), 0px 15px 40.02px rgba(0, 0, 0, 0.21);
  }
</style>