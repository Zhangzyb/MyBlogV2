<template>
  <div class="nav-wrap">
    <div class="nav-aside" :class="isShow ? 'show' : 'hide'">
      <div
        class="menu-btn"
        :class="isShow ? 'open' : 'close'"
        @click="menuClick"
      >
        <div class="line" :class="isShow ? 'top-line' : ''"></div>
        <div class="line" :class="isShow ? 'mid-line' : ''"></div>
        <div class="line" :class="isShow ? 'bot-line' : ''"></div>
      </div>
      <div class="search">
        <input type="text" placeholder="输入关键字" v-model="query" />
        <i class="iconfont iconsousuo" @click="searchClick"></i>
      </div>
      <div class="nav aside-con">
        <div class="note">导航</div>
        <nav-bar-item
          v-for="(item, index) in nav"
          :key="index"
          :path="item.path"
        >
          <a href="javascript:;"
            ><i class="iconfont" :class="item.class"></i>{{ item.name }}</a
          >
        </nav-bar-item>
      </div>
      <div class="tools aside-con">
        <div class="note">工具</div>
        <nav-bar-item v-for="(tool, index) in tools" :key="index">
          <a :href="tool.link" target="blank"
            ><i class="iconfont" :class="tool.class"></i>{{ tool.name }}</a
          >
        </nav-bar-item>
      </div>
    </div>
    <div :class="isShow ? 'mask' : 'mask-hide'" @click="isShow = false"></div>
  </div>
</template>

<script>
import NavBarItem from "components/common/navbar/NavBarItem";

export default {
  name: "Aside",
  data() {
    return {
      query: "",
      nav: [
        {
          class: "iconshouye",
          name: "首页",
          path: "/",
        },
        {
          class: "iconfenlei",
          name: "分类",
          path: "/category",
        },
        {
          class: "iconshiguangzhou",
          name: "时光轴",
          path: "/timeline",
        },
        {
          class: "iconpengyouquan",
          name: "个人动态",
          path: "/dynamic",
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
      isShow: false,
    };
  },
  methods: {
    menuClick() {
      this.isShow = !this.isShow;
    },
    searchClick() {
      if (!this.query) {
        this.$swal.fire({
          text: "请输入搜索内容",
          icon: "warning",
          showConfirmButton: false,
          timer: 1000,
        });
      } else {
        this.$router.push({
          path: "/search/",
          query: {
            text: this.query,
          },
        });
      }
    },
  },
  components: {
    NavBarItem,
  },
};
</script>

<style scoped>
@media screen and (max-width: 769px) {
  .nav-aside {
    position: fixed;
    width: 55vw;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 6rem 0.8rem 2rem 0.8rem;
    background: rgba(0, 0, 0, 0.801);
    transition: all 0.2s;
    z-index: 99;
  }
  .show {
    transform: translateX(0);
  }

  .hide {
    transform: translateX(-105%);
  }

  .menu-btn {
    position: absolute;
    top: 0.4rem;
    right: 1rem;
    width: 2.5rem;
    height: 36px;
    z-index: 999;
    cursor: pointer;
  }
  .menu-btn .line {
    position: absolute;
    width: 80%;
    height: 3px;
    background: rgb(255, 255, 255);
    margin: 0.8rem 0;
    transition: all 0.8s;
  }
  .top-line {
    top: 10px;
    transform: rotateZ(45deg);
  }
  .line:nth-child(2) {
    top: 10px;
  }

  .mid-line,
  .mask-hide {
    display: none;
  }

  .line:nth-child(3) {
    top: 20px;
  }

  .menu-btn .bot-line {
    top: 10px;
    transform: rotateZ(-45deg);
  }

  .close {
    transform: translateX(240%);
  }
  .open {
    transform: translateX(0);
  }

  .note {
    color: rgba(253, 253, 253, 0.767);
    font-size: 1.5rem;
  }
  .search {
    padding: 0 0.2rem;
  }

  .search input {
    height: 2.2rem;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    border-radius: 1rem;
  }

  .search i {
    top: 0;
    right: 1.2rem;
    height: 2.2rem;
    line-height: 2.2rem;
    font-size: 1.5rem;
  }
  .mask {
    position: fixed;
    width: 100vw;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: rgba(0, 0, 0, 0.3);
    z-index: 88;
  }
}

@media screen and (min-width: 770px) {
  .nav-wrap {
    flex: 1;
  }
  .nav-aside {
    position: relative;
    padding: 0 2rem 0 0;
  }

  .aside-con {
    border: 1px solid #e2e8ea;
  }

  .note {
    color: #6d7c83;
    font-size: 0.7rem;
  }
  .search {
    margin: 0 0 0.3rem 0;
    border: 1px solid #e2e8ea;
    border-radius: 0.5rem;
  }

  .search input {
    height: 1.5rem;
    font-size: 0.8rem;
    border-radius: 0.5rem;
  }
  .search i {
    top: 0.1rem;
    right: 0.5rem;
    height: 2rem;
    font-size: 1.1rem;
  }
}

.aside-con {
  padding-bottom: 0.6rem;
}

.note {
  padding: 0.5rem;
}

.search {
  position: relative;
  width: 100%;
  margin: 0 0 0.3rem 0;
  border-radius: 0.5rem;
}

.search input {
  width: 100%;
  border: none;
  outline: none;
  padding-left: 0.8rem;
  color: #1f2224cc;
}

.search i {
  position: absolute;
  display: block;
  color: #212121a1;
}
</style>