<template>
  <div class="post-detail">
    <Article :post="post" />
    <CommentList :comments="commentList" />
    <CommentBox :default="default_msg" />
  </div>
</template>

<script>
import Article from "./Article";
import CommentList from "./CommentList";
import CommentBox from "./comments/CommentBox";

import { getDetail, getComments } from "network/detail";

export default {
  name: "Detail",
  data() {
    return {
      post: {},
      commentList: [],
      id: null,
      default_msg: "说点什么吧",
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.getDetail();
    this.getComments();
    this.$bus.$off('addComment');
    this.$bus.$on('addComment', data => {
      this.commentList.unshift(data)
    })
  },
  methods: {
    getDetail() {
      getDetail(this.id).then((res) => {
        this.post = res.data;
      });
    },
    getComments() {
      getComments(this.id).then((res) => {
        this.commentList = res.data;
      });
    },
  },
  components: {
    Article,
    CommentList,
    CommentBox,
  },
};
</script>

<style scoped>
.post-detail {
  width: 100%;
  padding: 15px 25px;
  box-shadow: 0 0 20px 10px rgb(220 220 220 / 30%);
}
</style>