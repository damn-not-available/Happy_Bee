<template>
    <div class="container">
        <h2 style="margin-bottom:3%">비밀번호 수정</h2>
        <div style="width: 30%">
            <form @submit.prevent="updatePassword">
                <v-text-field
                    hint="바꿀 비밀번호를 입력하세요"
                    type="password"
                    :rules="[(v) => !!v || '비밀번호를 입력하세요']"
                    v-model.trim="new_password1"
                    :counter="20"
                    label="새로운 비밀번호"
                ></v-text-field>
                <v-text-field
                    hint="비밀번호를 동일하게 입력해주세요"
                    type="password"
                    :rules="[(v) => !!v || '비밀번호를 입력하세요']"
                    v-model.trim="new_password2"
                    :counter="20"
                    label="비밀번호 확인"
                ></v-text-field>
                
            <v-btn
            type="submit"
            >
            비밀번호 변경
            </v-btn>  
    </form>
    </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import {ref} from 'vue';
import { useCounterStore } from "@/stores/counter";
import { RouterLink, useRouter, useRoute } from "vue-router";

const store = useCounterStore();
const router = useRouter();
const new_password1 = ref(null);
const new_password2 = ref(null);

const updatePassword = ()=> {
    axios({
        method:'post',
        url: `${store.API_URL}/accounts/password/change/`,
        headers: { Authorization: `Token ${store.token}` },
        data:{
            new_password1 : new_password1.value,
            new_password2 : new_password2.value
        }
    }).then((res)=>{
        console.log('비밀번호 변경 완료!');
        router.push({ name: "ProfileView" });
    }).catch((err)=>{
        console.log(err);
    })
}
</script>

<style lang="scss" scoped>
.container {
  margin-top: 10%;
  margin-left: 15%;
}
</style>