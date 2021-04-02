<template>
  <div class="comment-list">
    <CommentItem
      v-for="(item, index) in comments"
      :key="item.id"
      :comment="item"
      :index="index"
      @agreeClick="addAgree(item)"
    />
  </div>
</template>

<script>
import CommentItem from "./comments/CommentItem";
import { addAgree } from "network/detail";

export default {
  name: "CommentsList",
  props: {
    comments: {
      type: Array,
    },
  },
  components: {
    CommentItem,
  },
  methods: {
    addAgree(item) {
      item.agree += 1
      const agree = item.agree;
      const data = {
        agree
      }
      addAgree(item.id, data);
    },
  },
};
</script>

<style scoped>
</style>