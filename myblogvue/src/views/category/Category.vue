<template>
  <div class="categories">
    <div class="cate-item" v-for="(cate, index) in categories" :key="index">
      <div class="cate-info">
        <div class="cate-head" @click="currentIndex = index">
          <span class="cate-name"> {{ cate.catename }}</span>
          <i class="iconfont iconyoujiantou" :class="currentIndex == index ? 'down' : ''"></i>
        </div>
        <ul class="post-list" v-show="currentIndex == index">
          <li v-for="(post, index) in cate.posts" :key="index">
            <a href="javascript:;">
              <span>{{ post.name }} </span>
              <span>{{ post.time }}</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Category",
  data() {
    return {
      categories: [
        {
          catename: "Python",
          posts: [
            { name: "Python中的多线程一", time: "2020-8-9" },
            { name: "Python中的多线程二", time: "2020-8-9" },
            { name: "Python中的多线程三", time: "2020-8-9" },
          ],
        },
        {
          catename: "Vue",
          posts: [
            { name: "Vue的响应式原理一", time: "2020-8-9" },
            { name: "Vue的响应式原理二", time: "2020-8-9" },
            { name: "Vue的响应式原理三", time: "2020-8-9" },
          ],
        },
      ],
      currentIndex: 0,
    };
  },
};
</script>

<style scoped>
.categories {
  width: 100%;
  color: #030303;
  border: 1px solid #e2e8ea;
}

.cate-head {
  display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    font-size: 1.2rem;
    cursor: pointer;
    background: #dfdede;
}

.cate-head i {
  margin-right: 1rem;
  font-size: 1.2rem;
  color: #030303;
  transition: all .3s;
}

.cate-name::before,
.cate-name::after {
  opacity: 0;
  display: inline-block;
  transition: transform 0.3s, opacity 0.2s;
}

.cate-name::before {
  content: "[";
  margin-right: 5px;
  transform: translateX(2rem);
}

.cate-name::after {
  content: "]";
  margin-left: 5px;
  transform: translateX(-2rem);
}

.cate-name:hover:before,
.cate-name:hover:after {
  opacity: 1;
  transform: translateX(0);
}

.post-list {
  transition: all 0.3s;
}

.post-list li {
  height: 2rem;
  line-height: 2rem;
}

.post-list a {
  display: flex;
  width: 100%;
  padding: 0 0 0 2rem;
  color: #212121a1;
  justify-content: space-between;
  transition: all 0.2s;
}

.post-list a:hover {
  background: rgba(0, 0, 0, 0.05);
}

.down{
    transform: rotate(90deg);
}
</style>