<template>
  <div class="dynamics">
    <div class="dynamic-item" v-for="(item, index) in messages" :key="index">
      <div class="dynamic-user">
        <div class="dynamic-avatar">
          <img :src="item.avatar" alt="头像" />
        </div>
        <div class="dynamic-info">
          <div class="dynamic-name">{{ item.username }}</div>
          <div class="dynamic-time">{{ item.created_time }}</div>
        </div>
      </div>
      <div class="dynamic-con">
        <div class="dynamic-mood">
          <p>{{ item.text }}</p>
        </div>
        <div class="dynamic-img" v-if="item.images">
          <img :src="item.images" alt="图片" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getDynamic } from "network/dynamic";

export default {
  name: "Dynamic",
  data() {
    return {
      messages: [],
    };
  },
  created() {
    this.getDynamic();
  },
  methods: {
    getDynamic() {
      getDynamic().then((res) => {
        this.messages = res.data.results;
      });
    },
  },
};
</script>

<style scoped>
.dynamics {
  width: 100%;
  box-shadow: 0 0 20px 10px rgb(220 220 220 / 30%);
}

.dynamic-item {
  margin: 0 0 1rem 0;
  padding: 0.8rem 1rem;
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
}

.dynamic-item:last-child {
  margin: 0;
}

.dynamic-user {
  display: flex;
}

.dynamic-avatar {
  width: 50px;
  height: 50px;
  margin-right: 0.5rem;
  border-radius: 50%;
}
.dynamic-avatar img {
  border-radius: 50%;
}

.dynamic-info {
  display: flex;
  flex-direction: column;
  font-size: 0.6rem;
  color: #212121a1;
  cursor: default;
}

.dynamic-name {
  margin: 0 0 0.3rem 0;
  color: #000;
  font-size: 1rem;
}

.dynamic-con {
  margin: 0.6rem 0 0;
}

.dynamic-mood {
  margin: 0 0 0.5rem 0;
}

.dynamic-img {
  width: 60%;
}
</style>