<template>
  <div class="timeline">
    <ul>
      <li v-for="(item, index) in timeData" :key="index">
        <div class="year">{{ item.time }}</div>
        <div class="time-item" v-for="obj in item.data" :key="obj.id">
          <div class="time-content">
            <p class="time-stamp">{{ obj.created_time }}</p>
            <h4>{{ obj.text }}</h4>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { getTimeData } from "network/timeline";

export default {
  name: "TimeLine",
  data() {
    return {
      timeData: [],
    };
  },
  created() {
    this.getTimeData()
  },
  methods: {
    getTimeData() {
      getTimeData().then((res) => {
        this.timeData = res.data;
      });
    },
  },
};
</script>

<style scoped>
.timeline {
  width: 100%;
  padding: 1rem 1.5rem;
  box-shadow: 0 0 20px 10px rgb(220 220 220 / 30%);
}

ul {
  list-style: none;
  position: relative;
  padding-left: 25px;
}

ul::before {
  content: "";
  position: absolute;
  width: 2px;
  top: 0;
  left: 0;
  bottom: 0;
  background: #d3d3d3;
}

ul li {
  margin-bottom: 1rem;
  border: 1px solid #ebeef5;
}

ul > li::before {
  content: "";
  width: 12px;
  height: 12px;
  background: #d3d3d3;
  border-radius: 50%;
  position: absolute;
  left: -5px;
}

.time-con {
  margin: 0.5rem 0;
  font-size: 0.8rem;
}

li span {
  color: #909399;
}

.time-content {
  color: #303133;
  padding: 20px;
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
}

.year {
  margin: 0 0 0.5rem 0;
}

.time-stamp {
  font-size: 0.9rem;
  padding: 0.2rem 0;
}

h4 {
  padding: 0.2rem 0;
  font-size: 0.9rem;
}

.time-item {
  margin-bottom: 10px;
}
</style>