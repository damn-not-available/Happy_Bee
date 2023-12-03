<template>
  <div class="container">
    <h2>적금상품 분류</h2>

    <v-select
      v-model.trim="select1"
      style="width: 30%"
      :items="banklist"
      density="compact"
      label="은행"
    ></v-select>

    <v-select
      v-model.trim="select2"
      style="width: 30%"
      :items="periodlist"
      density="compact"
      label="납입기간"
    >
    </v-select>

    <v-btn @click="saving_get_classified" style="margin-bottom: 2rem"
      >검색</v-btn
    >

    <div v-if="filteredoptions">
      <div v-if="filteredoptions.length == 0">
        <h3>조건에 해당하는 상품이 없습니다.</h3>
      </div>
      <v-row>
        <div v-for="filteredoption in filteredoptions" :key="filteredoption.id">
          <v-col style="padding: 2rem">
            <h5>
              <!-- {{
                deposits.find(
                  (deposit) => deposit.id === filteredoption.fin_prdt_cd
                ).fin_prdt_nm
              }} -->
            </h5>
            <p>저축 금리 [소수점 2자리] : {{ filteredoption.intr_rate }}</p>
            <p>
              최고 우대금리 [소수점 2자리] : {{ filteredoption.intr_rate2 }}
            </p>
            <p>저축 금리 유형 : {{ filteredoption.intr_rate_type }}</p>
            <p>저축 금리 유형명 : {{ filteredoption.intr_rate_type_nm }}</p>
            <p>저축 기간 [단위: 개월] : {{ filteredoption.save_trm }}</p>

            <p>
              <RouterLink
                :to="{
                  name: 'DepositDetail',
                  params: {
                    id: savings.find(
                      (deposit) => deposit.id === filteredoption.fin_prdt_cd
                    ).id,
                  },
                }"
                ><v-btn>자세히 보기</v-btn></RouterLink
              >
            </p>
          </v-col>
        </div>
      </v-row>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { RouterLink } from "vue-router";
import { useCounterStore } from "@/stores/product";
import axios from "axios";

const store = useCounterStore();
onMounted(() => {
  store.saveOptions();
});

const banklist = [...new Set(store.savings.map((item) => item.kor_co_nm))]; // 은행 리스트
const periodlist = [
  ...new Set(store.savingoptions.map((item) => item.save_trm)),
]; // 기간 리스트

const select1 = ref("-"); // bank
const select2 = ref("-"); // period
const filteredoptions = ref(null);
const savings = store.savings;

const API_URL = "http://127.0.0.1:8000";
const saving_get_classified = function () {
  axios({
    method: "post",
    url: `${API_URL}/products/saving_get_classified/`,
    data: {
      bank: select1.value,
      period: select2.value,
    },
  })
    .then((res) => {
      console.log(res.data);
      filteredoptions.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
};
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
