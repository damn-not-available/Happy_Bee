<template>
  <div class="container">
    <canvas id="myChart"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const userId = store.userId;
const user = ref(null);
const recommend_product = ref([]);
const my_product = ref([]);

const count = computed(() => {
  return my_product.value.length;
});

const names = ref([]);
const rate = ref([]);

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/profile/${userId}/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      user.value = res.data;
      axios({
        method: "post",
        url: `${store.API_URL}/products/personal_recommend/`,
        data: {
          user: user.value,
        },
      })
        .then((res) => {
          recommend_product.value = res.data;

          let num1 = recommend_product.value.recommend_money.length;
          let num2 = recommend_product.value.recommend_salary.length;
          my_product.value.length = 0;
          const set = new Set();
          for (let i = 0; i < num1; i++) {
            axios({
              method: "get",
              url: `${store.API_URL}/products/test/${recommend_product.value.recommend_money[i]}`,
            })
              .then((res) => {
                if (!set.has(recommend_product.value.recommend_money[i])) {
                  console.log(res.data);
                  my_product.value.push(res.data);
                  names.value.push(res.data.fin_prdt_nm);
                  rate.value.push(res.data.savingoptions_set[0].intr_rate2);
                  rate.value.push(res.data.depositoptions_set[0].intr_rate2);
                  set.add(recommend_product.value.recommend_money[i]);
                }
              })
              .catch((err) => {
                console.log(err);
              });
          }
          for (let i = 0; i < num2; i++) {
            axios({
              method: "get",
              url: `${store.API_URL}/products/test/${recommend_product.value.recommend_salary[i]}`,
            })
              .then((res) => {
                if (!set.has(recommend_product.value.recommend_salary[i])) {
                  console.log(res.data);
                  my_product.value.push(res.data);
                  names.value.push(res.data.fin_prdt_nm);
                  rate.value.push(res.data.savingoptions_set[0].intr_rate2);
                  rate.value.push(res.data.depositoptions_set[0].intr_rate2);
                  set.add(recommend_product.value.recommend_salary[i]);
                }
              })
              .catch((err) => {
                console.log(err);
              });
          }

          console.log(my_product.value[0]);
        })
        .catch((err) => {
          console.log(err);
        });
    })
    .catch((err) => {
      console.log(userId);
      console.log(err);
    });
});

document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("myChart");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "헤이(Hey)적금(정액적립식)",
        "JB 카드 재테크 적금\n(정기적립식)",
        "J정기예금\n(만기지급식)",
        "헤이(Hey)정기예금",
      ],
      datasets: [
        {
          label: "내가 가입한 상품 비교",
          data: [2.1, 1.9, 3.0, 4.2, 2.3, 3.5],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});
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
