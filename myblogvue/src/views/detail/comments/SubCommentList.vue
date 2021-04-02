<template>
  <div class="sub-comment-list">
    <SubCommentItem
      v-for="(item, index) in subcommentlist"
      :key="index"
      :subcomment="item"
      :parentIndex="commentIndex"
    />
  </div>
</template>

<script>
import SubCommentItem from "./SubCommentItem";

export default {
  name: "SubCommentList",
  props: {
    subcommentlist: {
      type: Array,
      default() {
        return [];
      },
    },
    commentIndex: {
      type: Number,
    },
  },
  components: {
    SubCommentItem,
  },
};
</script>

<style scoped>
</style>