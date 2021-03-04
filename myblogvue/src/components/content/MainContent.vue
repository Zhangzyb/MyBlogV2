<template>
<div class="main-con">
  <router-view></router-view>
</div>
</template>

<script>
export default {
  name: "MainContent"
  }
</script>

<style  scoped>
.main-con{
  flex: 3;
  display: flex;
  flex-flow: wrap;
  align-content: space-between;
  padding: 0 20px;
}
</style>