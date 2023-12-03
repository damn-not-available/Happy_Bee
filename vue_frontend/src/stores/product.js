import { ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore(
  "product",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const deposits = ref([]);
    const savings = ref([]);
    const depositoptions = ref([]);
    const savingoptions = ref([]);

    const saveProducts = function () {
      axios({
        method: "get",
        url: `${API_URL}/products/save_products/`,
      })
        .then(() => {
          axios({
            method: "get",
            url: `${API_URL}/products/savings/`,
          })
            .then((res) => {
              savings.value = res.data;
              axios({
                method: "get",
                url: `${API_URL}/products/deposits/`,
              })
                .then((res) => {
                  deposits.value = res.data;
                })
                .catch((err) => {
                  console.log(err);
                });
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const saveOptions = function () {
      axios({
        method: "get",
        url: `${API_URL}/products/deposit_options_all/`,
      })
        .then((res) => {
          depositoptions.value = res.data;
        })
        .then(() => {
          axios({
            method: "get",
            url: `${API_URL}/products/saving_options_all/`,
          })
            .then((res) => {
              savingoptions.value = res.data;
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      saveProducts,
      savings,
      deposits,
      saveOptions,
      depositoptions,
      savingoptions,
    };
  },
  { persist: true }
);
