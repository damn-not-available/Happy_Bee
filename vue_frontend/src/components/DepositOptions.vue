<template>
  <div style="margin-top: 15vh"></div>
  <div v-for="item in deposit.depositoptions_set" :key="item.id">
    <v-card variant="tonal">
      <v-card-title style="font-weight: 600; font-size: 20px"
        >{{ deposit.fin_prdt_nm }}상품의 옵션</v-card-title
      >
      <v-card-subtitle>{{ deposit.kor_co_nm }}</v-card-subtitle>
      <v-card-text>
        <p>저축 금리 [소수점 2자리] : {{ item.intr_rate }}</p>
        <p>최고 우대금리 [소수점 2자리] : {{ item.intr_rate2 }}</p>
        <p>저축 금리 유형 : {{ item.intr_rate_type }}</p>
        <p>저축 금리 유형명 : {{ item.intr_rate_type_nm }}</p>
        <p>저축 기간 [단위: 개월] : {{ item.save_trm }}</p>
      </v-card-text>
    </v-card>
  </div>
  <RouterLink :to="{ name: 'DepositDetail', params: { id: deposit.id } }"
    ><v-btn>뒤로 가기</v-btn></RouterLink
  >
  <RouterView />
</template>

<script setup>
import { onBeforeMount, ref } from "vue";
import { RouterView, RouterLink } from "vue-router";
import { useCounterStore } from "@/stores/product";
import { useRoute } from "vue-router";

const store = useCounterStore();
const route = useRoute();
const deposit = ref(null);
const deposit_pk = `${route.params.id}`;

onBeforeMount(() => {
  store.deposits.filter((item) => {
    if (item.id == deposit_pk) {
      deposit.value = item;
    }
  });
});
</script>

<style scoped>
h3 {
  font-weight: 600;
  margin-bottom: 20px;
}

.card {
  margin: auto;
}
* {
  margin: 1.5rem;
}
</style>
