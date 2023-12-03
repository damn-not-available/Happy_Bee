<template>
  <div>
    <div style="margin-top: 10%">
      <div style="width: 80%; margin: auto">
        <form @submit.prevent="createArticle">
          <v-select
            v-model.trim="category"
            style="padding-right: 1rem"
            :items="categories"
            density="compact"
            label="카테고리"
            hint="카테고리를 선택하세요"
          ></v-select>
          <v-text-field
            hint="제목을 입력하세요"
            v-model.trim="title"
            :counter="10"
            label="제목"
          ></v-text-field>

          <v-textarea
            hint="내용을 입력하세요"
            v-model.trim="content"
            :counter="100"
            label="내용"
          ></v-textarea>
          <v-btn class="me-4" type="submit"> 작성하기 </v-btn>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const category = ref(null);
const title = ref(null);
const content = ref(null);
const store = useCounterStore();
const router = useRouter();
const categories = ["은행", "금융상품", "일상"];

const createArticle = function () {
  if (category.value == "은행") {
    category.value = 1;
  } else if (category.value == "금융상품") {
    category.value = 2;
  } else {
    category.value = 3;
  }
  axios({
    method: "post",
    url: `${store.API_URL}/articles/`,
    data: {
      category: category.value,
      title: title.value,
      content: content.value,
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
</script>

<style scoped></style>
