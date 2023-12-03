<template>
  <div>
    <v-container>
      <v-row style="width: 80%; margin-top: 10%">
        <v-col cols="7">
          <h2>게시글 목록</h2>
        </v-col>
        <v-col cols="5">
          <RouterLink :to="{ name: 'CreateArticle' }">글 쓰기</RouterLink>
        </v-col>
      </v-row>

      <v-row style="width: 80%">
        <v-col cols="7">
          <v-select
            v-model="category"
            style="padding-right: 1rem"
            :items="items"
            density="compact"
            label="카테고리"
          ></v-select>
        </v-col>
        <v-col cols="5">
          <v-btn @click="updateArticles">적용</v-btn>
        </v-col>
      </v-row>
      <v-row v-if="category">
        <v-col v-if="category == '전체'">전체 조회입니다</v-col>
        <v-col v-else>{{ category }}와(과) 관련된 글입니다</v-col>
      </v-row>
      <v-row v-else><v-col>카테고리가 적용되지 않았습니다</v-col></v-row>
      <v-row>
        <ArticleListItem
          v-for="article in store.articles"
          :key="article.id"
          :article="article"
        ></ArticleListItem>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { ref, onMounted, onUpdated } from "vue";
import { useCounterStore } from "@/stores/counter";
import ArticleListItem from "@/components/ArticleListItem.vue";
import axios from "axios";
const items = ["전체", "은행", "금융상품", "일상"];
const store = useCounterStore();
const articles = ref([]);
const category = ref(null);

onMounted(() => {
  store.getArticles();
  articles.value = store.articles;
});

onUpdated(() => {
  articles.value = store.articles;
});
const updateArticles = function () {
  if (category.value == "은행") {
    category.value = 1;
  } else if (category.value == "금융상품") {
    category.value = 2;
  } else if (category.value == "일상") {
    category.value = 3;
  }
  if (category.value == "전체") {
    articles.value = store.articles;
  } else {
    axios({
      method: "get",
      url: `${store.API_URL}/articles/category/${category.value}/`,
    })
      .then((res) => {
        articles.value = res.data;
        if (category.value == 1) {
          category.value = "은행";
        } else if (category.value == 2) {
          category.value = "금융상품";
        } else {
          category.value = "일상";
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
};
</script>

<style scoped>
div {
}
</style>
