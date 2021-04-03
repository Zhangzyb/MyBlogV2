<template>
  <div class="post-item">
    <img :src="articleItem.image" alt="文章图片" />
    <div class="post-info">
      <div class="post-title" @click="detailClick(articleItem.id)">
        {{ articleItem.title }}
      </div>
      <div class="post-brief">{{ articleItem.abstract }}</div>
      <div class="post-state">
        <div><i class="iconfont iconrili"></i>&nbsp;{{ articleItem.time_format }}</div>
        <div>
          <i class="iconfont iconpinglun"></i>&nbsp;{{ articleItem.comment_num }}
        </div>
        <div><i class="iconfont iconremen"></i>&nbsp;{{ articleItem.views }}</div>
        <div><i class="iconfont iconaixin"></i>&nbsp;{{ articleItem.likes }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ArticleItem",
  props: {
    articleItem: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  methods: {
    detailClick(id) {
      this.$router.push("/post/" + id);
    },
  },
};
</script>

<style scoped>
.post-item {
  position: relative;
  width: 100%;
  height: 15rem;
  color: #fff;
  margin-bottom: 3rem;
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

.post-title:hover{
  cursor: pointer;
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

.load-more {
  width: 10rem;
  margin: 0 auto 1rem;
  padding: 0.5rem;
  text-align: center;
  border-radius: 2rem;
  background: #5d63636e;
  cursor: pointer;
  transition: all 0.2s;
}

.load-more:hover {
  color: #fff;
  text-shadow: 0 0 10px rgb(255 255 255 / 50%);
  background: #5d6363a4;
}
</style>

