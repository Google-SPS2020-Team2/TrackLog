<template>
  <div id="userLogin">
    <h1>Login to TrackLog</h1>
    <md-field>
      <label>Username</label>
      <md-input v-model="username"></md-input>
    </md-field>
    <md-field>
      <label>Password</label>
      <md-input v-model="password" type="password"></md-input>
    </md-field>
    <md-button style="float: right;" v-on:click="login()">Login</md-button>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
  data: function () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      this.$http.post('/login', {
        username: this.username,
        password: this.password
      })
          .then(() => {
            this.$store.commit('userLogin', this.username);
            this.$router.push({path: '/'});
          })
          .catch(err => {
            console.error(err);
          })
    }
  }
}
</script>

<style scoped>
#userLogin {
  max-width: 300px;
}
</style>