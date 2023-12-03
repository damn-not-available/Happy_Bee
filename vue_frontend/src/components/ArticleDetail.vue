<template>
  <div style="margin-top: 10%">
    <div v-if="article">
      <v-card variant="tonal" justify="center" style="margin: 2rem; width: 80%">
        <v-card-item>
          <v-card-title style="font-weight: 600">
            {{ article.title }}
          </v-card-title>
          <v-card-text>
            <p style="margin-bottom: 1rem">{{ article.content }}</p>
            <p style="margin-bottom: 1rem">작성자 {{ article.user }}번 유저</p>
            <p style="margin-bottom: 1rem">
              작성일자 {{ article.created_at.slice(0, 10) }}
            </p>
            <p style="margin-bottom: 1rem">
              수정일자 {{ article.updated_at.slice(0, 10) }}
            </p>
          </v-card-text>
          <div v-if="isWriter">
            <v-btn
              size="small"
              variant="tonal"
              @click="deleteArticle(article.id)"
              style="margin-right: 1rem"
              >삭제하기</v-btn
            >

            <RouterLink
              :to="{ name: 'UpdateArticle', params: { id: article.id } }"
              ><v-btn size="small" variant="tonal">수정하기</v-btn></RouterLink
            >
          </div>
        </v-card-item>
      </v-card>
    </div>
    <div v-else>로딩중입니다</div>
    <RouterLink :to="{ name: 'ArticleView' }"
      ><v-btn
        size="small"
        variant="tonal"
        style="margin-left: 2rem; margin-bottom: 2rem"
        >뒤로 가기</v-btn
      ></RouterLink
    >
    <div class="container">
      <RouterView />
      <div>
        <div style="margin-left: 2rem">
          <p style="margin-bottom: 3px">{{ comment_count }}개의 댓글</p>
        </div>
        <form @submit.prevent="createComment">
          <v-row style="width: 50%">
            <v-col cols="10">
              <v-text-field
                clearable
                label="댓글을 달아주세요!"
                variant="underlined"
                v-model.trim="content"
                style="margin-left: 2rem"
              ></v-text-field>
            </v-col>
            <v-col cols="2">
              <v-btn variant="tonal" type="submit">작성</v-btn>
            </v-col>
          </v-row>
        </form>
      </div>
      <div v-if="articleComments">
        <div
          style="margin-left: 2rem; margin-bottom: 1rem"
          v-for="comment in articleComments"
          :key="comment.id"
        >
          <span>{{ comment.user }}번 유저: </span>
          <span style="margin-right: 1rem">{{ comment.content }}</span>
          <span
            v-if="comment.user == curUser"
            @click.prevent="deleteComment(comment.id)"
          >
            <v-btn size="small" variant="tonal">삭제</v-btn></span
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, computed } from "vue";
import { RouterView, RouterLink } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const comment_count = ref(null);
const articleComments = ref(null);
const content = ref(null);
const writer = ref(null);
const token = store.token;
const curUser = store.userId;

const isWriter = computed(() => {
  return curUser == writer.value;
});

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: { Authorization: `Token ${token}` },
    data: {
      content: content.value,
    },
  })
    .then((res) => {
      console.log(res);
      article.value = res.data;
      writer.value = res.data.user;
      comment_count.value = res.data.comment_count;
      articleComments.value = res.data.comments;
    })
    .catch((err) => {
      // print(route.params.id);
      console.log(err);
    });
});

const deleteArticle = function () {
  axios({
    method: "delete",
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      article.value = res.data;
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};

const createComment = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/articles/${route.params.id}/comments/`,
    headers: { Authorization: `Token ${store.token}` },
    data: {
      content: content.value,
    },
  })
    .then((res) => {
      axios({
        method: "get",
        url: `${store.API_URL}/articles/${route.params.id}/`,
        headers: { Authorization: `Token ${token}` },
      })
        .then((res) => {
          articleComments.value = res.data.comments;
          content.value = "";
        })
        .catch((err) => {
          console.log(err);
        });
    })
    .catch((err) => {
      console.log(err);
    });
};

const deleteComment = function (comment_id) {
  axios({
    method: "delete",
    url: `${store.API_URL}/articles/${route.params.id}/comments/${comment_id}`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      axios({
        method: "get",
        url: `${store.API_URL}/articles/${route.params.id}/`,
        headers: { Authorization: `Token ${token}` },
      })
        .then((res) => {
          articleComments.value = res.data.comments;
        })
        .catch((err) => {
          console.log(err);
        });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
h3 {
  font-weight: 600;
  margin-bottom: 20px;
}
</style>
