<template>
  <div class="card">
    <div v-if="deposit">
      <v-card variant="tonal">
        <v-card-title style="font-weight: 600; font-size: 30px">{{
          deposit.fin_prdt_nm
        }}</v-card-title>
        <v-card-subtitle>{{ deposit.kor_co_nm }}</v-card-subtitle>
        <v-card-text>
          <p>가입제한: {{ join_deny }}</p>
          <p>가입대상: {{ deposit.join_member }}</p>
          <p>가입방법: {{ deposit.join_way }}</p>
          <p>우대조건: {{ deposit.spcl_cnd }}</p>
          <p>
            최고한도: {{ deposit.max_limit ? deposit.max_limit : "한도 없음" }}
          </p>
          <p>옵션 갯수 : {{ deposit.depositoptions_set.length }}개</p>

          <RouterLink
            :to="{ name: 'DepositOptions', params: { id: deposit_pk } }"
            style="margin-left: 0"
            ><v-btn>옵션 자세히 보기</v-btn></RouterLink
          >
        </v-card-text>
      </v-card>
    </div>
    <div v-else>로딩 중입니다</div>
    <RouterLink :to="{ name: 'DepositsView' }" style="margin-left: 1.8rem"
      ><v-btn>뒤로 가기</v-btn></RouterLink
    >

    <RouterView />
  </div>
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
const join_deny = ref(null);
onBeforeMount(() => {
  store.deposits.filter((item) => {
    if (item.id == deposit_pk) {
      deposit.value = item;
      join_deny.value =
        deposit.value.join_deny == 1
          ? "제한 없음"
          : deposit.value.join_deny == 2
          ? "서민 전용"
          : "일부 제한";
    }
  });
});
</script>

<style scoped>
.card {
  margin-top: 15vh;
  margin-right: auto;
  margin-left: auto;
}
* {
  margin: 2rem;
}
</style>
