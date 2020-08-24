<template>
  <footer
    class="footer"
    :class="{ [`footer-${type}`]: type }"
    :data-background-color="backgroundColor"
  >
    <div class="container">
      <nav>
        <ul>
          <li>
            <a href="https://github.com/Google-SPS2020-Team2">
              SPS Mainland Team 2
            </a>
          </li>
          <li>
            <a href="https://sites.google.com/google.com/sps-gcn/">
              About Us
            </a>
          </li>
        </ul>
      </nav>
      <div class="copyright">
        &copy; {{ year }}, made by
        <a href="https://github.com/Google-SPS2020-Team2/" target="_blank">SPS Mainland Team 2</a>.
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  props: {
    backgroundColor: String,
    type: String
  },
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style></style>
