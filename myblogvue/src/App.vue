<template>
  <div id="app">
    <Header />
     <Main />
    <Footer />
  </div>
</template>

<script>
import Header from "components/content/Header";
import Main from "components/content/Main";
import Footer from "components/content/Footer";

export default {
  name: "App",
  components: {
    Header,
    Main,
    Footer
  },
};
</script>

<style>
@import "assets/css/base.css";
@import "assets/css/index.css";
</style>
