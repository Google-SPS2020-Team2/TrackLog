<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Your Story Starts With Us.</h1>
            <h4>
              Log your track, follow the progress. Join us and write your story here.
            </h4>
            <br />
            <md-button to="/login"
              class="md-success md-lg"
              >Login</md-button
            >
          </div>
        </div>
      </div>
    </parallax>
    <div></div>
  </div>
</template>

<script>
export default {
  name:'Welcome',
  bodyClass: "landing-page",
  props: {
    header: {
      type: String,
      default: require("@/assets/img/bg7.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  }
};
</script>

<style lang="scss" scoped>
.md-card-actions.text-center {
  display: flex;
  justify-content: center !important;
}
.contact-form {
  margin-top: 30px;
}

.md-has-textarea + .md-layout {
  margin-top: 15px;
}
</style>

