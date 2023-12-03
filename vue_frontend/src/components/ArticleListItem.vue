<template>
  <v-col cols="3">
    <v-card variant="tonal" justify="center">
      <v-card-item color="black">
        <v-card-title>
          {{ article.title }}
        </v-card-title>
        <v-card-text>
          {{ article.content }}
        </v-card-text>
        <v-card-actions>
          <v-btn
            ><RouterLink
              :to="{ name: 'ArticleDetail', params: { id: article.id } }"
            >
              자세히보기
            </RouterLink></v-btn
          >
        </v-card-actions>
      </v-card-item>
    </v-card>
  </v-col>
</template>

<script setup>
import { RouterLink } from "vue-router";

const props = defineProps({
  article: Object,
});
</script>

<style scoped>
#text-black {
  color: black;
  background-color: #ffe082;
  width: 30vw;
}
</style>
