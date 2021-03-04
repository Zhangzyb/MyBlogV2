<template>
<div>
    <div class="post-item" v-for="post in posts" :key="post.time">
      <img src="~assets/img/1.webp" alt="文章图片" />
      <div class="post-info">
        <div class="post-title">{{post.title}}</div>
        <div class="post-brief">{{post.brief}}</div>
        <div class="post-state">
          <div><i class="iconfont iconrili"></i>&nbsp;{{post.time}}</div>
          <div><i class="iconfont iconpinglun"></i>{{post.comment}}</div>
          <div><i class="iconfont iconremen"></i>{{post.views}}</div>
          <div><i class="iconfont iconaixin"></i>{{post.likes}}</div>
        </div>
      </div>
    </div>
    </div>
</template>

<script>

export default {
  name: "Home",
  data() {
      return {
          posts: [
              {
                  pic: "~assets/img/1.jpg",
                  title: "Vue+Django前后端分离",
                  brief: "vue作为一个渐进式的js框架通过其易学习，亦儒门的优点得到广大用户的青睐,vue作为一个渐进式的js框架通过其易学习，亦儒门的优点得到广大用户的青睐",
                  time: "2019-10-3",
                  comment: 3,
                  views: 5,
                  likes: 5
              }
          ]
      }
  }
};
</script>

<style scoped>
.post-item {
  position: relative;
  width: 100%;
  height: 14rem;
  color: #fff;
  margin-bottom: 20px;
  border-radius: 0.5rem;
  border: 1px solid #e2e8ea;
  overflow: hidden;
}

.post-item img {
  height: 100%;
  object-fit: cover;
  transition: all 0.5s;
}

.post-item:hover img {
  transform: scale(1.2);
  filter: blur(3px);
}

.post-info {
  display: flex;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
  justify-content: center;
  align-content: space-evenly;
  flex-wrap: wrap;
}

.post-title {
  width: 100%;
  text-align: center;
  font-size: 1.2rem;
  text-shadow: 0 0 10px rgb(255 255 255 / 50%);
  transition: all 0.5s;
}

.post-brief {
  opacity: 0;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  width: 80%;
  margin-top: 1.5rem;
  overflow: hidden;
  transition: all 0.5s;
}

.post-state {
  opacity: 0;
  display: flex;
  width: 75%;
  justify-content: space-evenly;
  text-align: center;
  transition: all 0.5s;
}

.post-state > div {
  flex: 1;
}

.post-item:hover .post-brief {
  opacity: 1;
}

.post-item:hover .post-state {
  opacity: 1;
}

.iconrili {
  color: rgb(247, 163, 68);
  font-size: 1rem;
}
.iconpinglun {
  color: yellowgreen;
  font-size: 1.1rem;
}
.iconremen {
  color: red;
  font-size: 1.2rem;
}
.iconaixin {
  color: #ff6767;
  font-size: 1rem;
  display: inline-block;
  padding-top: 3px;
}
</style>