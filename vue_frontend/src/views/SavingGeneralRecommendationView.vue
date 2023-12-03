<template>
  <div class="container">
    <h2>적금 일반 추천</h2>
    <div v-if="saving_recommend">
      <v-select
        v-model.trim="option"
        style="width: 30%"
        :items="items"
        density="compact"
        label="검색조건"
      ></v-select>
      <v-btn @click="applyOption">적용</v-btn>

      <!-- 상품이 여러개일 때 -->
      <div v-if="count != 0">
        <div v-if="count > 1" v-for="item in product" :key="item.id">
          {{ item.kor_co_nm }}의 {{ item.fin_prdt_nm }}
          <RouterLink
            :to="{
              name: 'DepositDetail',
              params: {
                id: item.id,
              },
            }"
          >
            <v-btn size="small">자세히 보기</v-btn>
          </RouterLink>
        </div>
        <!-- 상품이 1개 이하일 때 -->
        <div v-else>
          <!-- 상품이 1개일 때 -->
          <div v-if="count == undefined">
            {{ product.kor_co_nm }}의 {{ product.fin_prdt_nm }}

            <RouterLink
              :to="{
                name: 'SavingDetail',
                params: {
                  id: product.id,
                },
              }"
            >
              <v-btn size="small">자세히 보기</v-btn>
            </RouterLink>
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
import { onMounted, ref, computed } from "vue";
import { RouterLink } from "vue-router";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
const saving_recommend = ref([]);
const product = ref([]);
const count = computed(() => {
  return product.value.length;
});
const items = [
  "최고우대금리",
  "랜덤돌리기",
  "신규가입",
  "인터넷가입우대",
  "금액한도제한없음",
];
const option = ref(null);
const applyOption = () => {
  if (option.value == "최고우대금리") {
    product.value = saving_recommend.value.saving_product_highest_intr_rate2;
  } else if (option.value == "랜덤돌리기") {
    axios({
      method: "get",
      url: `${API_URL}/products/random_saving/`,
    })
      .then((res) => {
        product.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  } else if (option.value == "신규가입") {
    product.value = saving_recommend.value.saving_new_signup;
  } else if (option.value == "인터넷가입우대") {
    product.value = saving_recommend.value.saving_internet_signup;
  } else {
    product.value = saving_recommend.value.saving_unlimited;
  }
};
const get_saving_general_recommendation = function () {
  axios({
    method: "get",
    url: `${API_URL}/products/saving_general_recommendation/`,
  })
    .then((res) => {
      console.log(res.data);
      saving_recommend.value = res.data;
    })
    .catch((err) => {
      console.log("적금 못 받았다!");
      console.log(err);
    });
};

onMounted(() => {
  get_saving_general_recommendation();
});
</script>

<style scoped>
.container {
  margin-top: 10%;
  margin-left: 10%;
}
* {
  margin-bottom: 1rem;
}
</style>
