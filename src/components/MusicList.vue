<template>
  <p @click="fetchMusic">Music list page</p>
</template>

<script>
export default {
  name: "MusicList",
  methods: {
    fetchMusic() {
      this.$http.get('/show')
        .then(res => console.log(res.data))
        .catch(err => console.error(err));
    }
  }
}
</script>

<style scoped>

</style>