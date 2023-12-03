<template>
  <div class="body">
    <v-container>
      <h2 style="margin-bottom: 2rem">내 주변 은행 찾기</h2>
      <v-row>
        <v-select
          v-model="province"
          @change="updateCities"
          style="padding-right: 1rem"
          :items="items"
          density="compact"
          label="도/시"
        >
          <!-- <option value="">도/시</option>
          <option v-for="info in infos" :key="info.id">
            {{ info.prov }}
          </option> -->
        </v-select>
        <v-select
          v-model="city"
          style="padding-right: 1rem"
          :items="cities"
          density="compact"
          label="시/군/구"
        >
          <!-- <option value="">도/시</option>
          <option v-for="info in infos" :key="info.id">
            {{ info.prov }}
          </option> -->
        </v-select>
        <v-select
          v-model="bank"
          style="padding-right: 1rem"
          :items="banks"
          density="compact"
          label="은행명"
        >
          <!-- <option value="">도/시</option>
          <option v-for="info in infos" :key="info.id">
            {{ info.prov }}
          </option> -->
        </v-select>

        <!-- <select v-model="province" @change="updateCities">
          <option value="">도/시</option>
          <option v-for="info in infos" :key="info.id">
            {{ info.prov }}
          </option>
        </select>
        <select v-model="city">
          <option value="">시/군/구</option>
          <option v-for="c in cities" :key="c">{{ c }}</option>
        </select>
        <select v-model="bank">
          <option value="">은행명</option>
          <option v-for="b in banks" :key="b">{{ b }}</option>
        </select> -->
      </v-row>
      <v-row>
        <v-col>
          <MapComponent :province="province" :city="city" :bank="bank" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import MapComponent from "@/components/MapComponent.vue";
import { ref, watch } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();

const infos = store.infos;
const items = ref([]);

for (let i = 0; i < infos.length; i++) {
  items.value.push(infos[i].prov);
}

const banks = store.banks;
const cities = ref([]);

const province = ref("");
const city = ref("");
const bank = ref("");

const updateCities = () => {
  const selectedInfo = infos.find((info) => info.prov === province.value);
  cities.value = selectedInfo ? selectedInfo.city : [];
};

watch(province, () => {
  updateCities();
});

updateCities();
</script>

<style>
.body {
  margin-top: 8%;
}
</style>
