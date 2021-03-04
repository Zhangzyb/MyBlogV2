<template>
  <div class="aside-item" @click="navClick" :class="isActive ? 'active':'' ">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "NavBarItem",
  computed: {
    isActive() {
      return this.$route.path == this.path
    }
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
.aside-item {
  display: flex;
  height: 2rem;
  align-items: center;
  justify-content: center;
  width: 100%;
  font-size: 0.8rem;
  transition: all 0.3s;
  cursor: pointer;
}
.aside-item:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.aside-item a {
  width: 100%;
  padding-left: 1.2rem;
  color: #212121a1;
}

.aside-item a i {
  margin-right: 1rem;
  font-size: 1rem;
}

.active{
  background: rgba(0, 0, 0, 0.05);
}
</style>