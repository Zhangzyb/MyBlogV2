<template>
  <div class="main-con">
    <keep-alive exclude="Detail,Search">
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: "MainContent",
};
</script>

<style  scoped>
.main-con {
  flex: 3;
  display: flex;
  justify-content: center;
}
</style>