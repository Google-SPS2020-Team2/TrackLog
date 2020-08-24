<template>
  <div v-bind:id="'comment-' + comment.id " style="margin-bottom: 1rem;">
    <md-list-item>
      <div class = "comment-text">
        <span class="md-title" >{{ comment.player_id }}</span>
        <p class="md-info">
          {{ comment.content }}
        </p>
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
</style>