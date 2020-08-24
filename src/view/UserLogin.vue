<template>
  <div class="wrapper">
    <div class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-33 md-small-size-66 md-xsmall-size-100 md-medium-size-40 mx-auto"
          >
            <login-card header-color="green">
              <h4 slot="title" class="card-title">Login to TrackLog</h4>
              <p slot="description" class="description">Start your journey here</p>
              <md-field class="md-form-group" slot="inputs">
                <md-icon>account_circle</md-icon>
                <label>Username...</label>
                <md-input v-model="username"></md-input>
              </md-field>
              <md-field class="md-form-group" slot="inputs" v-if="isRegister">
                <md-icon>face</md-icon>
                <label>Nickname...</label>
                <md-input v-model="nickname"></md-input>
              </md-field>
              <md-field class="md-form-group" slot="inputs">
                <md-icon>lock_outline</md-icon>
                <label>Password...</label>
                <md-input v-model="password"></md-input>
              </md-field>
              <md-button slot="footer" v-on:click="isRegister = !isRegister">
                <span v-if="isRegister">Login</span>
                <span v-else>Register</span>
              </md-button>
              <md-button slot="footer" v-if="isRegister"
                        class="md-raised md-success float-right"
                        v-on:click="register()">
                Submit
              </md-button>
              <md-button slot="footer" v-else
                        class="md-raised md-success float-right"
                        v-on:click="login()">
                Login
              </md-button>
            </login-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { LoginCard } from "@/components";

export default {
  name: "UserLogin",
  components: {
    LoginCard
  },
  bodyClass: "login-page",
  data: function () {
    return {
      isRegister: false,
      username: '',
      nickname: '',
      password: ''
    }
  },
  props: {
    header: {
      type: String,
      default: require("@/assets/img/profile_city.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
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
            this.$router.push({path: '/music'});
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