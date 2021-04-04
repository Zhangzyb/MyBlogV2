<template>
  <div class="search">
    <div class="search-res" v-if="results.length" >
      <h3 class="search-note">{{ finalResult }}</h3>
      <CategoryItem :articles="results" />
    </div>
    <div class="no-result" v-else></div>
  </div>
</template>

<script>
import CategoryItem from "components/content/CategoryItem";
import { getSearchResult } from "network/search";

export default {
  name: "Search",
  data() {
    return {
      results: [],
      query: this.$route.query.text,
    };
  },
  computed: {
    finalResult() {
      return this.$route.query.text + "的搜索结果：";
    },
  },
  created() {
    this.getSearchResult(this.query);
  },
  methods: {
    getSearchResult(query) {
      getSearchResult(query).then((res) => {
        this.results = res.data;
      });
    },
  },
  watch: {
    $route() {
      this.getSearchResult(this.$route.query.text);
    },
  },
  components: {
    CategoryItem,
  },
};
</script>

<style scoped>
.search {
  width: 100%;
  padding: 1rem 1.2rem;
  box-shadow: 0 0 20px 10px rgb(220 220 220 / 30%);
}

.search-note {
  margin: 0 0 1rem 0;
}

.no-result {
  width: 100%;
  height: 100%;
  background: url("~assets/img/no-results.svg") no-repeat center;
  background-size: cover;
}
</style>