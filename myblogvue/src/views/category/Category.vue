<template>
  <div class="categories">
    <div class="cate-item" v-for="(item, index) in categories" :key="index">
      <div class="cate-head" @click="currentIndex = index">
        <span class="cate-name"> {{ item.category }}</span>
        <i class="iconfont iconyoujiantou"></i>
      </div>
      <div class="cate-posts" v-if="currentIndex == index">
        <CategoryItem :articles="item.data"/>
      </div>
    </div>
  </div>
</template>

<script>
import CategoryItem from 'components/content/CategoryItem'
import { getCategory } from "network/category";

export default {
  name: "Category",
  data() {
    return {
      categories: [],
      currentIndex: 0,
    };
  },
  components:{
    CategoryItem
  },
  created() {
    this.getCategory();
  },
  methods: {
    getCategory() {
      getCategory().then((res) => {
        this.categories = res.data;
      });
    },
   
  },
};
</script>

<style scoped>
.categories {
  width: 100%;
  color: #030303;
  padding: 0.5rem 0.5rem 0;
  box-shadow: 0 0 20px 10px rgb(220 220 220 / 30%);
}

.cate-head {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0 0.5rem 0.8rem;
  font-size: 1.2rem;
  background: linear-gradient(45deg, #89898914, #e2e8ea);
  cursor: pointer;
  border-left: 6px solid #0000001a;
}

.cate-head i {
  margin-right: 1rem;
  font-size: 1.2rem;
  color: #030303;
  transition: all 0.2s;
}

.cate-head:hover {
  background: linear-gradient(45deg, #898989, #e7edef);
  border-left: 6px solid #000000a1;
}

.cate-posts {
  padding: 0.5rem 1rem;
}
</style>