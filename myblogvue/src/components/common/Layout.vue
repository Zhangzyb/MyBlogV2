<template>
  <div class="container">
    <div class="header"><slot name="header"></slot></div>
    <div class="main"><slot name="main"></slot></div>
    <div class="footer"><slot name="footer"></slot></div>
  </div>
</template>

<script>
export default {
  name: "Layout",
  components: {},
};
</script>

<style>
@keyframes head-anim {
  to {
    background-position: 400% 0;
  }
}

.header {
  display: flex;
  height: 16vw;
  min-height: 230px;
  color: #fff;
  font-size: 1.6rem;
  background-color: #7eb;
  text-shadow: 0 0 10px rgb(255 255 255 / 50%);
  background-image: linear-gradient(
    to right,
    #9cf 0%,
    #f9c 25%,
    #ec8 50%,
    #7eb 75%,
    #9cf 100%
  );
  background-size: 400% 100%;
  animation: head-anim 30s linear infinite;
}

.main{
  display: flex;
  width: 80vw;
  margin: 0 auto;
  padding: 20px 0;
}
</style>