<template>
  <div class="container">
    <h2>개인 맞춤 추천</h2>
    <v-btn @click="test">TEST</v-btn>
    <div v-if="my_product">
      <!-- 상품이 여러개일 때 -->
      <div v-if="count != 0">
        <div v-if="count > 1" v-for="item in my_product" :key="item.id">
          {{ item.kor_co_nm }}의 {{ item.fin_prdt_nm }}
        </div>
        <!-- 상품이 1개 이하일 때 -->
        <div v-else>
          <!-- 상품이 1개일 때 -->
          <div v-if="count == undefined">
            {{ my_product.kor_co_nm }}의 {{ my_product.fin_prdt_nm }}
          </div>
          <!-- 선택된 상품이 없을 때 -->
          <div v-else>선택한 상품이 없습니다</div>
        </div>
      </div>
      <div v-else>선택한 상품이 없습니다</div>
    </div>
    <div v-else style="margin: 10%">로딩중입니다..!</div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const userId = store.userId;
const user = ref(null);
const recommend_product = ref(null);
const my_product = ref([]);

const count = computed(() => {
  return my_product.value.length;
});

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/profile/${userId}/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      user.value = res.data;
    })
    .catch((err) => {
      console.log(userId);
      console.log(err);
    });
});

const test = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/products/personal_recommend/`,
    data: {
      user: user.value,
    },
  })
    .then((res) => {
      recommend_product.value = res.data;
      let num1 = recommend_product.value.recommend_money.length;
      let num2 = recommend_product.value.recommend_salary.length;
      my_product.value.length = 0;
      const set = new Set();
      for (let i = 0; i < num1; i++) {
        axios({
          method: "get",
          url: `${store.API_URL}/products/test/${recommend_product.value.recommend_money[i]}`,
        })
          .then((res) => {
            if (!set.has(recommend_product.value.recommend_money[i])) {
              console.log(set.length);
              my_product.value.push(res.data);
              set.add(recommend_product.value.recommend_money[i]);
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
      for (let i = 0; i < num2; i++) {
        axios({
          method: "get",
          url: `${store.API_URL}/products/test/${recommend_product.value.recommend_salary[i]}`,
        })
          .then((res) => {
            if (!set.has(recommend_product.value.recommend_salary[i])) {
              console.log(set.length);
              my_product.value.push(res.data);
              set.add(recommend_product.value.recommend_salary[i]);
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style lang="scss" scoped>
.container {
  margin-top: 10%;
  margin-left: 10%;
}
* {
  margin-bottom: 1rem;
}
</style>
