<template>
  <div class="container">
    <div v-if="user">
      <h2 style="margin-bottom: 1.5rem">{{ user.username }}님의 프로필</h2>
      <v-row>
        <v-col cols="5">
          <v-list lines="one">
            <v-list-item>성: {{ user.first_name }}</v-list-item>
            <v-list-item>이름: {{ user.last_name }}</v-list-item>
            <v-list-item>나이: {{ user.age }}</v-list-item>
            <v-list-item>닉네임: {{ user.nickname }}</v-list-item>
            <v-list-item>자산: {{ user.money }}</v-list-item>
            <v-list-item>연봉: {{ user.salary }}</v-list-item>
            <v-list-item>주소: {{ user.address }}</v-list-item>
            <v-list-item style="margin-bottom: 1rem"
              >위험회피성향: {{ user.risk_aversion }}</v-list-item
            >
          </v-list>
        </v-col>
        <v-col cols="5" style="margin-top: 10%">
          <!-- <v-img
            :width="300"
            aspect-ratio="16/9"
            src="../../assets/profile.png"
          ></v-img> -->
          <v-row style="margin-bottom: 5%">
            <RouterLink :to="{ name: 'UserChart' }">
              <v-btn>내 차트 보기</v-btn>
            </RouterLink></v-row
          >
          <v-row style="margin-bottom: 5%">
            <RouterLink :to="{ name: 'UpdateProfile' }">
              <v-btn>프로필 수정</v-btn>
            </RouterLink></v-row
          >
          <v-row>
            <RouterLink :to="{ name: 'UpdatePassword' }">
              <v-btn>비밀번호 수정</v-btn>
            </RouterLink></v-row
          >
        </v-col>
      </v-row>
    </div>
    <div v-else>로딩중입니다</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const userId = store.userId;
const user = ref(null);

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
</script>

<style scoped>
p {
  padding: 1rem;
}

.container {
  margin-top: 10%;
  margin-left: 15%;
}
</style>
