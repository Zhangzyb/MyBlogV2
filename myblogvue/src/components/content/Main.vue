<template>
  <div class="main">
    <div class="m-wrap">
      <NavBar />
      <MainContent />
    </div>
  </div>
</template>

<script>
import MainContent from "components/content/MainContent";
import NavBar from "components/common/navbar/NavBar";

export default {
  name: "Main",
  components: {
    NavBar,
    MainContent,
  },
};
</script>

<style scoped>
@media screen and (max-width: 992px) {
  .main {
    width: 90vw;
  }
}

@media screen and (min-width: 993px) {
  .main {
    width: 70vw;
  }
}

.main {
  flex: 1;
  display: flex;
  margin: 0 auto;
  padding: 20px 0;
}

.m-wrap {
  display: flex;
  width: 100%;
  justify-content: space-between;
}
</style>