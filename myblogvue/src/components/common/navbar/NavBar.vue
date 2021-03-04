<template>
  <div class="nav-aside">
    <div class="search">
      <input type="text" placeholder="输入关键字" />
      <i class="iconfont iconsousuo"></i>
    </div>
    <div class="nav aside-con">
      <div class="note">导航</div>
      <nav-bar-item v-for="(item, index) in nav" :key="index" :path="item.path">
        <a href="javascript:;"><i class="iconfont" :class="item.class"></i>{{ item.name }}</a>
      </nav-bar-item>
    </div>
    <div class="tools aside-con">
      <div class="note">工具</div>
      <nav-bar-item v-for="(tool, index) in tools" :key="index">
        <a :href="tool.link" target="blank"><i class="iconfont" :class="tool.class"></i>{{ tool.name }}</a>
      </nav-bar-item>
    </div>
  </div>
</template>

<script>
import NavBarItem from './NavBarItem'

export default {
  name: "Aside",
  data() {
    return {
      nav: [
        {
          class: "iconshouye",
          name: "首页",
          path: '/'
        },
        {
          class: "iconfenlei",
          name: "分类",
          path: '/category'
        },
        {
          class: "iconshiguangzhou",
          name: "时光轴",
          path: '/timeline'
        },
        {
          class: "iconpengyouquan",
          name: "个人动态",
          path: '/dynamic'
        },
      ],
      tools: [
        {
          class: "iconGitHub",
          name: "Github",
          link: "https://github.com/Zhangzyb",
        },
        {
          class: "iconjianxiu",
          name: "Clip-path Maker",
          link: "https://www.html.cn/tool/css-clip-path/",
        },
        {
          class: "icontupian",
          name: "Big-jpg",
          link: "https://bigjpg.com/",
        },
        {
          class: "iconshezhi",
          name: "Iconfont",
          link: "https://www.iconfont.cn/",
        },
      ],
    };
  },
  methods: {
    navClick() {
      this.$router.replace("/category");
    },
  },
  components: {
    NavBarItem
  }
};
</script>

<style scoped>
.nav-aside {
  flex: 1;
}

.aside-con {
  border: 1px solid #e2e8ea;
  padding-bottom: 0.6rem;
}

.note {
  padding: 0.5rem;
  color: #6d7c83;
  font-size: 0.7rem;
}

.search {
  position: relative;
  width: 100%;
  margin: 0 0 0.3rem 0;
  border: 1px solid #e2e8ea;
  border-radius: 0.5rem;
}

.search input {
  width: 100%;
  height: 1.5rem;
  padding-left: 0.8rem;
  border: none;
  outline: none;
  font-size: 0.8rem;
  color: #1f2224cc;
  border-radius: 0.5rem;
}

.search i {
  position: absolute;
  display: block;
  top: 0.1rem;
  right: 0.5rem;
  height: 2rem;
  color: #212121a1;
  font-size: 1.1rem;
}

</style>