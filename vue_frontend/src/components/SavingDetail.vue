<template>
  <div class="card">
    <div v-if="saving">
      <v-card variant="tonal">
        <v-card-title style="font-weight: 600; font-size: 30px">{{
          saving.fin_prdt_nm
        }}</v-card-title>
        <v-card-subtitle>{{ saving.kor_co_nm }}</v-card-subtitle>
        <v-card-text>
          <p>가입제한: {{ join_deny }}</p>
          <p>가입대상: {{ saving.join_member }}</p>
          <p>가입방법: {{ saving.join_way }}</p>
          <p>우대조건: {{ saving.spcl_cnd }}</p>
          <p>
            최고한도: {{ saving.max_limit ? saving.max_limit : "한도 없음" }}
          </p>
          <p>옵션 갯수 : {{ saving.savingoptions_set.length }}개</p>

          <RouterLink
            :to="{ name: 'SavingOptions', params: { id: saving.id } }"
            style="margin-left: 0"
            ><v-btn>옵션 자세히 보기</v-btn></RouterLink
          >
        </v-card-text>
      </v-card>
    </div>
    <div v-else>로딩 중입니다</div>

    <RouterLink :to="{ name: 'SavingsView' }" style="margin-left: 1.8rem"
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
const saving = ref(null);
const saving_pk = `${route.params.id}`;
const join_deny =
  saving.join_deny == 1
    ? "제한 없음"
    : saving.join_deny == 2
    ? "서민 전용"
    : "일부 제한";
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
.card {
  margin-top: 15vh;
  margin-right: auto;
  margin-left: auto;
}
* {
  margin: 2rem;
}
</style>
