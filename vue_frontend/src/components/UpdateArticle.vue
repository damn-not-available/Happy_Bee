<template>
  <div style="margin-top: 10%">
    <div v-if="article">
      <div style="width: 80%; margin: auto">
        <form @submit.prevent="updateArticle">
          <v-text-field
            hint="제목을 입력하세요"
            :rules="[(v) => !!v || '제목을 입력하세요']"
            v-model.trim="article.title"
            :counter="10"
            label="제목"
          ></v-text-field>

          <v-textarea
            hint="내용을 입력하세요"
            :rules="[(v) => !!v || '내용을 입력하세요']"
            v-model.trim="article.content"
            :counter="100"
            label="내용"
          ></v-textarea>
          <v-btn class="me-4" type="submit"> 수정하기 </v-btn>
          <v-btn @click="resetAll"> 지우기 </v-btn>
        </form>
      </div>
    </div>
    <div v-else>로딩중입니다</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink, useRouter, useRoute } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const article = ref(null);
const router = useRouter();
const route = useRoute();

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      article.value = res.data;
      console.log(article.value);
    })
    .catch((err) => {
      print(route.params.id);
      console.log(err);
    });
});

const updateArticle = function () {
  axios({
    method: "put",
    url: `${store.API_URL}/articles/${route.params.id}/`,
    data: {
      title: article.value.title,
      content: article.value.content,
    },
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};
const resetAll = () => {
  article.value.title = "";
  article.value.content = "";
};
</script>

<style scoped></style>
