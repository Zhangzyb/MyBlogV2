<template>
<div class="header">
  <div class="head-info">
    <div class="head-img">
      <img src="~assets/img/headimg.jpg" alt="个人头像" />
    </div>
    <div class="head-title">Zhangzyb</div>
    <div class="head-text">总有人会被梦想抛弃</div>
  </div>
</div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
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

.head-info {
  display: flex;
  width: 50%;
  margin: 0 auto;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.head-img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
img {
  border-radius: 50%;
  cursor: pointer;
}
img:hover {
  transform: rotate(360deg);
  transition-duration: 1.2s;
  box-shadow: 0 0 10px rgb(255 255 255 / 50%);
}
.head-title {
  color: #fff;
  margin-top: 0.2rem;
  font-weight: 700;
  padding: 0;
  text-shadow: 0 0 10px rgb(255 255 255 / 50%);
  user-select: none;
}

.head-text {
  margin-top: 0.6rem;
  font-size: 1.2rem;
  user-select: none;
}
</style>