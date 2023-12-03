<template>
  <ArticleList />
  <RouterView />
</template>

<script setup>
import { onMounted, onUpdated, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import ArticleList from "@/components/ArticleList.vue";

const store = useCounterStore();
const articles = ref(null);

onMounted(() => {
  store.getArticles();
  console.log(store);
  console.log(store.articles);
  articles.value = store.articles;
});
</script>

<style scoped>
.articles {
  margin-top: 5%;
}
</style>
