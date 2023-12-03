<template>
  <div>
    <button @click="test">TEST</button>
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

const test = function () {
  console.log(user.value);
  axios({
    method: "post",
    url: `${store.API_URL}/products/personal_recommend/`,
    data: {
      user: user.value,
    },
  })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style lang="scss" scoped></style>
