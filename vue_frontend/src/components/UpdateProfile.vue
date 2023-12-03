<template>
  <div class="container">
    <div style="margin-top: 10%">
      <div v-if="user">
        <div style="width: 30%">
          <form @submit.prevent="updateProfile">
            <v-text-field
              hint="성을 입력하세요"
              :rules="[(v) => !!v || '성을 입력하세요']"
              v-model.trim="user.first_name"
              :counter="10"
              label="성"
            ></v-text-field>
            <v-text-field
              hint="이름을 입력하세요"
              :rules="[(v) => !!v || '이름을 입력하세요']"
              v-model.trim="user.last_name"
              :counter="10"
              label="이름"
            ></v-text-field>

            <v-text-field
              hint="나이를 입력하세요"
              :rules="[(v) => !!v || '나이을 입력하세요']"
              type="number"
              v-model.trim="user.age"
              :counter="10"
              label="나이"
            ></v-text-field>

            <v-text-field
              hint="닉네임을 입력하세요"
              :rules="[(v) => !!v || '닉네임을 입력하세요']"
              v-model.trim="user.nickname"
              :counter="10"
              label="닉네임"
            ></v-text-field>

            <v-text-field
              hint="자산을 입력하세요"
              :rules="[(v) => !!v || '자산을 입력하세요']"
              v-model.trim="user.money"
              type="number"
              :counter="10"
              label="자산"
            ></v-text-field>

            <v-text-field
              hint="연봉을 입력하세요"
              :rules="[(v) => !!v || '연봉을 입력하세요']"
              v-model.trim="user.salary"
              type="number"
              :counter="10"
              label="연봉"
            ></v-text-field>
            <v-text-field
              hint="주소를 입력하세요"
              :rules="[(v) => !!v || '주소를 입력하세요']"
              v-model.trim="user.address"
              :counter="10"
              label="주소"
            ></v-text-field>
            <v-select
              v-model="user.risk_aversion"
              :items="items"
              :rules="[(v) => !!v || '위험회피성향을 선택해주세요']"
              label="위험회피성향"
              required
            >
            </v-select>
            <v-btn class="me-4" type="submit"> 수정하기 </v-btn>
          </form>
        </div>
      </div>
      <div v-else>로딩중입니다</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink, useRouter, useRoute } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const router = useRouter();
const route = useRoute();

const userId = store.userId;
const user = ref(null);
const items = ["위험회피", "위험중립", "위험선호"];

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/profile/${userId}/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      user.value = res.data;
      console.log(res);
    })
    .catch((err) => {
      console.log(userId);
      console.log(err);
    });
});

const updateProfile = function () {
  if (user.value.risk_aversion == "위험회피") {
    user.value.risk_aversion = 1;
  } else if (user.value.risk_aversion == "위험중립") {
    user.value.risk_aversion = 2;
  } else {
    user.value.risk_aversion = 3;
  }
  axios({
    method: "put",
    url: `${store.API_URL}/profile/${store.userId}/`,
    data: {
      first_name: user.value.first_name,
      last_name: user.value.last_name,
      age: user.value.age,
      nickname: user.value.nickname,
      money: user.value.money,
      salary: user.value.salary,
      address: user.value.address,
      risk_aversion: user.value.risk_aversion,
    },
  })
    .then((res) => {
      console.log("수정성공");
      router.push({ name: "ProfileView" });
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
