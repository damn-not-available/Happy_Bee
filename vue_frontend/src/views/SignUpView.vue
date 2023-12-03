<template>
  <h2 style="text-align: center; margin-top: 15%">회원가입</h2>
  <v-sheet width="300" class="mx-auto" style="background-color: transparent">
    <v-form ref="form" @submit.prevent="signUp">
      <v-text-field
        v-model="username"
        :counter="10"
        :rules="[(n) => !!n || '아이디를 입력하세요']"
        label="username"
        required
      ></v-text-field>
      <v-text-field
        v-model="password1"
        type="password"
        :counter="20"
        :rules="[(n) => !!n || '비밀번호를 입력하세요']"
        label="password"
        required
      ></v-text-field>
      <v-text-field
        v-model="password2"
        type="password"
        :counter="20"
        :rules="[(n) => !!n || '비밀번호를 입력하세요']"
        label="password 확인"
        required
      ></v-text-field>
      <v-text-field
        v-model="age"
        type="number"
        :counter="10"
        :rules="[(n) => !!n || '나이를 입력하세요']"
        label="나이"
        required
      ></v-text-field>
      <v-text-field
        v-model="money"
        type="number"
        :counter="20"
        :rules="[(n) => !!n || '자산을 입력하세요']"
        label="자산"
        required
      ></v-text-field>
      <v-text-field
        v-model="salary"
        type="number"
        :counter="20"
        :rules="[(n) => !!n || '연봉을 입력하세요']"
        label="연봉"
        required
      ></v-text-field>
      <v-text-field
        v-model="nickname"
        :counter="10"
        :rules="[(n) => !!n || '닉네임을 입력하세요']"
        label="닉네임"
        required
      ></v-text-field>
      <v-text-field
        v-model="address"
        :counter="20"
        :rules="[(n) => !!n || '주소를 입력하세요']"
        label="주소"
        required
      ></v-text-field>
      <v-select
        v-model="risk_aversion"
        :items="items"
        :rules="[(v) => !!v || '위험회피성향을 선택해주세요']"
        label="위험회피성향"
        required
      >
      </v-select>

      <v-btn color="#e6a01e" class="mt-4" type="submit"> 가입하기 </v-btn>
    </v-form>
  </v-sheet>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const age = ref(null);
const money = ref(null);
const salary = ref(null);
const nickname = ref(null);
const address = ref(null);
const risk_aversion = ref(null);
const items = ["위험회피", "위험중립", "위험선호"];
const profile_img = ref(null);

const signUp = function () {
  if (risk_aversion.value == "위험회피") {
    risk_aversion.value = 1;
  } else if (risk_aversion == "위험중립") {
    risk_aversion.value = 2;
  } else {
    risk_aversion.value = 3;
  }
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    nickname: nickname.value,
    address: address.value,
    risk_aversion: risk_aversion.value,
    profile_img: profile_img.value,
  };

  store.signUp(payload);
};
</script>

<style lang="scss" scoped>
body {
  padding: 0;
  margin: 0;
}
.vid-container {
  position: relative;
  height: 150vh;
  overflow: hidden;
}
.bgvid.back {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: -100;
}
.inner {
  position: absolute;
}
.inner-container {
  width: 400px;
  height: 400px;
  position: absolute;
  top: calc(50vh - 200px);
  left: calc(50vw - 200px);
  overflow: hidden;
}
.bgvid.inner {
  top: calc(-50vh + 200px);
  left: calc(-50vw + 200px);
  filter: url("data:image/svg+xml;utf9,<svg%20version='1.1'%20xmlns='http://www.w3.org/2000/svg'><filter%20id='blur'><feGaussianBlur%20stdDeviation='10'%20/></filter></svg>#blur");
  -webkit-filter: blur(10px);
  -ms-filter: blur(10px);
  -o-filter: blur(10px);
  filter: blur(10px);
}
.box {
  position: absolute;
  height: 100%;
  width: 100%;
  font-family: Helvetica;
  color: #222222;
  background: rgb(231, 36, 36), 0;
  padding: 30px 0px;
}
.box h1 {
  text-align: center;
  margin: 30px 0;
  font-size: 30px;
}
.box input,
select {
  display: block;
  width: 300px;
  margin: 20px auto;
  padding: 15px;
  background: rgba(250, 207, 88, 0.2);
  color: #383838;
  border: 0;
}
.box input:focus,
.box input:active,
.box button:focus,
.box button:active {
  outline: none;
}
.box button {
  background: #e6a01e;
  border: 0;
  color: #292929;
  padding: 10px;
  font-size: 20px;
  width: 300px;
  margin: 20px auto;
  display: block;
  cursor: pointer;
}
.box button:hover {
  background: rgb(179, 179, 179), 160, 39;
}
.box p {
  font-size: 14px;
  text-align: center;
}
.box p span {
  cursor: pointer;
  color: #666;
}
</style>
