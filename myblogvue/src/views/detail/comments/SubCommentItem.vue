<template>
  <div class="sub-comment-item">
    <div class="sub-avatar">
      <img :src="subcomment.avatar" alt="头像" />
    </div>
    <div class="sub-comment-con">
      <div class="sub-comment-user">
        <span>{{ subcomment.username }} </span>
        <span class="reply-name"> {{ subcomment.reply_name }}</span>
        <span class="sub-comment-text">{{ subcomment.text }}</span>
      </div>
      <div class="sub-comment-info">
        <div class="sub-comment-time">{{ subcomment.created_time }}</div>
        <div class="sub-attitude">
          <span
            ><i class="iconfont icongood-fill"></i>{{ subcomment.agree }}</span
          >
          <span
            ><i class="iconfont iconbad-fill"></i
            >{{ subcomment.disagree }}</span
          >
        </div>
        <div class="sub-reply" @click="subReply">回复</div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "SubCommentItem",
  props: {
    subcomment: {
      type: Object,
      default() {
        return {};
      },
    },
    parentIndex: {
      type: Number,
    },
  },
  methods: {
    subReply() {
      const payload = {
        parentIndex: this.parentIndex,
        reply_name: this.subcomment.username,
      };
      this.$store.commit("subClick", payload);
    },
  }
};
</script>

<style scoped>
.sub-comment-item {
  display: flex;
  padding: 0.8rem 0 0 0;
  font-size: 1rem;
}

.sub-avatar {
  width: 1.5rem;
  height: 1.5rem;
  margin: 0 0.8rem 0 0;
}

.sub-comment-con {
  width: 100%;
}

.sub-comment-user {
  padding: 0 0 0.5rem 0;
}

.reply-name {
  color: #00a1d6;
}

.sub-comment-text {
  word-break: break-all;
  padding-bottom: 0.3rem;
  line-height: 1.3;
  letter-spacing: 2px;
  font-size: 0.9rem;
}

.sub-comment-info {
  display: flex;
  font-size: 0.8rem;
  color: #0000007a;
}

.sub-comment-time {
  margin-right: 1rem;
  cursor: default;
}

.sub-attitude span {
  margin-right: 1rem;
}

.sub-attitude span:hover i,
.sub-reply:hover {
  color: #00a1d6;
}

.sub-attitude span i {
  margin-right: 5px;
  cursor: pointer;
}

.sub-reply {
  cursor: pointer;
}
</style>