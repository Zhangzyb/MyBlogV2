<template>
  <div class="aside-item" @click="navClick" :class="isActive ? 'active' : ''">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "NavBarItem",
  computed: {
    isActive() {
      return this.$route.path == this.path;
    },
  },
  props: {
    path: String,
  },
  methods: {
    navClick() {
      if (this.$route.path !== this.path) {
        this.$router.push(this.path);
      }
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 769px) {
  .aside-item {
    font-size: 1.3rem;
    padding: 1.8rem 0.6rem; 
  }
  .aside-item a {
    color: #fff;
    text-shadow: 0 0 10px rgb(255 255 255 / 50%);
  }
  .aside-item a i {
    margin-right: 1.6rem;
    font-size: 1.6rem;
  }
}

@media screen and (min-width: 770px) {
  .aside-item {
    font-size: 0.8rem;
  }
  .aside-item a {
    color: #212121a1;
  }
  .aside-item:hover {
    background-color: rgba(0, 0, 0, 0.05);
  }
  .active {
    background: rgba(0, 0, 0, 0.05);
  }
  .aside-item a i {
    margin-right: 1rem;
    font-size: 1rem;
  }
}

.aside-item {
  display: flex;
  height: 2rem;
  align-items: center;
  justify-content: center;
  width: 100%;
  transition: all 0.3s;
  cursor: pointer;
}

.aside-item a {
  width: 100%;
  padding-left: 1.2rem;
}
</style>