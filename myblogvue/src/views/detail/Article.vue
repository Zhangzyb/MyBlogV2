<template>
  <div>
    <h2 class="article-title">{{ post.title }}</h2>
    <div class="article-info">
      <span>
        <i class="iconfont iconshijian"></i>{{ post.created_time }}</span
      >
      <span><i class="iconfont iconremen"></i>阅读:{{ post.views }}</span>
      <span
        ><i class="iconfont iconpinglun"></i>评论:{{ post.comment_num }}</span
      >
      <span><i class="iconfont iconaixin"></i>喜欢:{{ post.likes }}</span>
    </div>
    <div class="article-body">
      <vue-markdown :source="post.content"></vue-markdown>
    </div>
    <div class="article-footer">
      <div class="tags">
        标签:
        <span v-for="(tag, index) in post.tag_info" :key="index"
          ><i class="iconfont iconbiaoqian"></i> {{ tag.name }}</span
        >
      </div>
      <div class="article-cate">
        分类:
        <span><i class="iconfont iconbiaoqian"></i> {{ post.category }}</span>
        <span class="like" @click="show"
          ><i class="iconfont iconaixin"></i
        ></span>
      </div>
    </div>
    <div v-if="post.comment_num > 0" class="comment-num">
      已收到{{ post.comment_num }}条评论
    </div>
    <div v-else class="comment-num">暂无评论</div>
    <div class="alert" :class="{ 'alert-anima': isShow }">赞 过 了</div>
  </div>
</template>

<script>
import VueMarkdown from "@adapttive/vue-markdown";
import Prism from "prismjs";
import "prismjs/prism";
import "prismjs/themes/prism.css";
import "prismjs/themes/prism-okaidia.css";
import "prismjs/components/prism-javascript";

export default {
  name: "Article",
  props: {
    post: "",
  },
  data() {
    return {
      isShow: false,
    };
  },
  components: {
    VueMarkdown,
  },
  methods: {
    update: function () {
      this.$nextTick(() => {
        Prism.highlightAll();
      });
    },
    show() {
      this.$swal.fire({
        width: 200,
        icon:'warning',
        text: "赞过了",
        showConfirmButton: false,
        timer: 1000,
      });
    },
  },
};
</script>

<style scoped>
.article-title {
  font-size: 1.8rem;
  color: #212121cc;
  text-align: center;
}

.article-info {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0.5rem 0 0.6rem 0;
  font-size: 0.8rem;
  color: #1f2224;
}

.article-info span {
  padding: 0.2rem;
}
.article-info span i {
  margin: 0 0.2rem;
  padding: 0;
}

.article-body p {
  text-indent: 2em;
  line-height: 1.6rem;
}

.article-footer {
  margin: 1.5rem 0 0 0;
  font-size: 0.8rem;
}

.tags {
  margin: 0 0 0.5rem 0;
}

.article-footer span {
  display: inline-block;
  margin: 0 0.2rem;
  padding: 0.2rem;
  color: azure;
  border-radius: 0.2rem;
  background: #6fa3ef;
}

.article-cate span {
  background: #e8a258;
}

.article-body {
  line-height: 1.8;
}

.article-cate span.like {
  float: right;
  background: #fff;
  width: 3.2rem;
  border: 2px solid rgb(241, 71, 105);
  text-align: center;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.article-cate span.like:hover {
  background: rgb(241, 71, 105);
}

.article-cate span.like:hover i {
  color: #fff;
}

.like i {
  color: rgb(241, 71, 105);
}

.comment-num {
  padding: 1rem 0;
  text-align: center;
}

@keyframes alert {
  0%,
  100% {
    transform: translateX(10rem);
  }
  50% {
    transform: translateX(0);
  }
}

.alert {
  display: none;
  position: fixed;
  top: 30vh;
  right: -0.3rem;
  width: 10rem;
  background: rgba(0, 0, 0, 0.801);
  color: #fff;
  padding: 0.5rem;
  text-align: center;
  transform: translateX(10rem);
}

.alert-anima {
  display: block;
  animation: alert 2s;
}
</style>