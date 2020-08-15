<template>
  <div id="user-login" style="margin: 20vh auto;">
    <h1>Login to TrackLog</h1>
    <md-field>
      <label>Username</label>
      <md-input v-model="username"></md-input>
    </md-field>
    <md-field v-if="isRegister">
      <label>Nickname</label>
      <md-input v-model="nickname"></md-input>
    </md-field>
    <md-field>
      <label>Password</label>
      <md-input v-model="password" type="password"></md-input>
    </md-field>
    <md-button v-on:click="isRegister = !isRegister">
      <span v-if="isRegister">Login</span>
      <span v-else>Register</span>
    </md-button>
    <md-button v-if="isRegister"
               class="md-raised md-primary float-right"
               v-on:click="register()">
      Submit
    </md-button>
    <md-button v-else
               class="md-raised md-primary float-right"
               v-on:click="login()">
      Login
    </md-button>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
  data: function () {
    return {
      isRegister: false,
      username: '',
      nickname: '',
      password: ''
    }
  },
  methods: {
    register() {
      this.$http.post('/register', {
        username: this.username,
        nickname: this.nickname,
        password: this.password
      })
          .then(() => {
            this.login();
          })
          .catch(err => {
            console.error(err);
          })
    },
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
#user-login {
  max-width: 300px;
}

.float-right {
  float: right;
}
</style>