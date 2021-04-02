<template>
  <div class="comment-item">
    <div class="comment-main">
      <div class="avatar">
        <img :src="comment.avatar" alt="头像" />
      </div>
      <div class="comment-con">
        <div class="comment-user">{{ comment.username }}</div>
        <div class="comment-text">
          <p>{{ comment.text }}</p>
        </div>
        <div class="comment-info">
          <div class="comment-time">{{ comment.created_time }}</div>
          <div class="attitude">
            <span @click="addAgree"
              ><i class="iconfont icongood-fill"></i>{{ comment.agree }}</span
            >
            <span
              ><i class="iconfont iconbad-fill"></i>{{ comment.disagree }}</span
            >
            <span @click="loadSubComment"
              ><i class="iconfont iconpinglun"></i
              >{{ comment.sub_comment_num }}</span
            >
          </div>
          <div class="reply" @click="replyBox(comment.username, index)">
            回复
          </div>
        </div>
        <SubCommentList
          :subcommentlist="subcommentlist"
          :commentIndex="index"
        />
        <CommentBox v-if="show()" :parent_comment="comment.id" />
      </div>
    </div>
  </div>
</template>

<script>
import CommentBox from "./CommentBox";
import SubCommentList from "./SubCommentList";

import { getSubComment } from "network/detail";

export default {
  name: "CommentItem",
  data() {
    return {
      subcommentlist: [],
      replyName: "",
      commentIdx: -1,
    };
  },
  props: {
    comment: {
      type: Object,
      defautl() {
        return {};
      },
    },
    index: {
      type: Number,
    },
  },
  components: {
    CommentBox,
    SubCommentList,
  },
  methods: {
    show() {
      return this.$store.state.currentIndex === this.index;
    },
    loadSubComment() {
      getSubComment(this.comment.id).then((res) => {
        this.subcommentlist = res.data;
      });
    },
    replyBox() {
      const payload = {
        reply_name: this.comment.username,
        index: this.index,
      };
      this.$store.commit("showReply", payload);
    },
    addAgree(){
      this.$emit('agreeClick')
    }
  },
  created(){
    this.$bus.$off('addSubComment');
    this.$bus.$on('addSubComment',data => {
      this.subcommentlist.unshift(data)
    })
  }
};
</script>

<style scoped>
.comment-main {
  display: flex;
  margin: 0 0 0rem 0;
  padding: 0.8rem 0 0 0;
}

.avatar {
  width: 2.1rem;
  height: 2.1rem;
  margin: 1rem 1.5rem 0 0;
}

.comment-con {
  width: 100%;
  padding: 0.8rem 0 0 0;
  border-top: 1px solid #e0e1e3;
}

.comment-user {
  padding: 0 0 0.5rem 0;
}

.comment-text p {
  word-break: break-all;
  padding-bottom: 0.5rem;
}

.comment-info {
  display: flex;
  font-size: 0.8rem;
  color: #0000007a;
}

.comment-time {
  margin-right: 1rem;
  cursor: default;
}

.attitude span {
  margin-right: 1rem;
}

.attitude span:hover i,
.reply:hover {
  color: #00a1d6;
}

.attitude span i {
  color: #0000007a;
  margin-right: 5px;
  cursor: pointer;
}

.reply {
  cursor: pointer;
}
</style>