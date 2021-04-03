<template>
  <div class="posts">
    <ArticleItem
      v-for="item in posts.list"
      :key="item.id"
      :articleItem="item"
    />
    <div class="load-over" v-if="loadFlag">到底了</div>
    <div class="load-more" @click="loadMore" v-else>加载更多</div>
  </div>
</template>

<script>
import { getHomePosts } from "network/home";
import ArticleItem from "./ArticleItem";

export default {
  name: "Home",
  data() {
    return {
      posts: { page: 0, list: [] },
      loadFlag: false,
    };
  },
  created() {
    this.getHomePosts();
  },
  methods: {
    getHomePosts() {
      const page = this.posts.page + 1;
      getHomePosts(page).then(
        (res) => {
          this.posts.list.push(...res.data.results);
          this.posts.page += 1;
        },
        (err) => {
          this.loadFlag = true;
        }
      );
    },
    loadMore() {
      if (!this.loadFlag) {
        this.getHomePosts();
      }
    },
  },
  components: {
    ArticleItem,
  },
};
</script>

<style scoped>
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

.load-over {
  text-align: center;
}
</style>