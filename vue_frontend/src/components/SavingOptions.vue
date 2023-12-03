<template>
  <div style="margin-top: 15vh"></div>
  <div v-for="item in saving.savingoptions_set" :key="item.id">
    <v-card variant="tonal">
      <v-card-title style="font-weight: 600; font-size: 20px"
        >{{ saving.fin_prdt_nm }}상품의 옵션</v-card-title
      >
      <v-card-subtitle>{{ saving.kor_co_nm }}</v-card-subtitle>
      <v-card-text>
        <p>저축 금리 [소수점 2자리] : {{ item.intr_rate }}</p>
        <p>최고 우대금리 [소수점 2자리] : {{ item.intr_rate2 }}</p>
        <p>저축 금리 유형 : {{ item.intr_rate_type }}</p>
        <p>저축 금리 유형명 : {{ item.intr_rate_type_nm }}</p>
        <p>저축 기간 [단위: 개월] : {{ item.save_trm }}</p>
        <p>적립 유형 : {{ item.rsrv_type }}</p>
        <p>적립 유형명: {{ item.rsrv_type_nm }}</p>
      </v-card-text>
    </v-card>
  </div>
  <RouterLink :to="{ name: 'SavingDetail', params: { id: saving_id } }"
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
const saving = ref(null);
const saving_pk = `${route.params.id}`;

onBeforeMount(() => {
  store.savings.filter((item) => {
    if (item.id == saving_pk) {
      console.log(item);
      saving.value = item;
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
