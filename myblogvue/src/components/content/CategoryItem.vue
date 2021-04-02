<template>
  <div>
    <div class="cate-post-item" v-for="(post, index) in articles" :key="index">
      <div class="cate-img">
        <img :src="post.image" alt="文章图片" />
      </div>
      <div class="cate-post-info">
        <h4
          class="post-title"
          @click="clickDetail(post.id)"
          v-html="post.title"
        ></h4>
        <p class="cate-brief" v-html="post.abstract"></p>
        <span class="cate-time">{{ post.created_time }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CategoryItem",
  props: {
    articles: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  methods: {
    clickDetail(id) {
      this.$router.push("/post/" + id);
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 992px) {
  .cate-brief {
    -webkit-line-clamp: 1;
  }
}

@media screen and (min-width: 993px) {
  .cate-brief {
    -webkit-line-clamp: 2;
  }
}

.cate-post-item {
  display: flex;
  padding-bottom: 0.4rem;
}

.cate-post-item:last-child {
  padding: 0;
}

.cate-img {
  flex: 1;
  margin-right: 1rem;
}

.cate-post-info {
  flex: 3;
}

.post-title:hover {
  cursor: pointer;
}

.cate-brief {
  display: -webkit-box;
  margin: 0.3rem 0;
  color: #212121;
  font-size: 0.8rem;
  text-overflow: ellipsis;
  overflow: hidden;
  -webkit-box-orient: vertical;
}

.cate-time {
  font-size: 0.7rem;
  color: #999;
}
</style>