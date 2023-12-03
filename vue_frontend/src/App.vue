<template>
  <nav id="primary_nav_wrap">
    <div class="logo">
      <RouterLink :to="{ name: 'MainView' }"
        ><h1 style="margin-right: 10px; color: #1c1c1c">
          Happy Bee
        </h1></RouterLink
      >
      <v-img :width="40" aspect-ratio="16/9" src="../assets/logo.png"></v-img>
    </div>

    <ul style="margin-top: 1rem">
      <!-- <li>
        <RouterLink :to="{ name: 'testView' }">실험실</RouterLink>
      </li> -->
      <li>
        <RouterLink :to="{ name: 'ArticleView' }">커뮤니티</RouterLink>
      </li>
      <li>
        <p>금융상품 전체보기</p>
        <ul>
          <li>
            <RouterLink :to="{ name: 'DepositsView' }"
              >예금상품 목록</RouterLink
            >
          </li>
          <li>
            <RouterLink :to="{ name: 'SavingsView' }">적금상품 목록</RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'DepositClassifyView' }"
              >예금상품 분류보기</RouterLink
            >
          </li>
          <li>
            <RouterLink :to="{ name: 'SavingClassifyView' }"
              >적금상품 분류보기</RouterLink
            >
          </li>
        </ul>
      </li>
      <li>
        <RouterLink :to="{ name: 'ExchangerView' }">환율계산기</RouterLink>
      </li>
      <li>
        <RouterLink :to="{ name: 'BankView' }">영업점 찾기</RouterLink>
      </li>
      <li>
        <a href="">금융상품추천</a>
        <ul>
          <li>
            <RouterLink :to="{ name: 'DepositGeneralRecommendationView' }"
              >예금 일반 추천</RouterLink
            >
          </li>
          <li>
            <RouterLink :to="{ name: 'SavingGeneralRecommendationView' }"
              >적금 일반 추천</RouterLink
            >
          </li>
          <div
            v-if="store.isLogin"
            style="display: flex; justify-content: space-between"
          >
            <li>
              <RouterLink :to="{ name: 'PersonalRecommendView' }"
                >개인맞춤</RouterLink
              >
            </li>
          </div>
        </ul>
      </li>
      <div
        v-if="store.isLogin"
        style="display: flex; justify-content: space-between"
      >
        <li>
          <RouterLink :to="{ name: 'ProfileView' }">마이페이지</RouterLink>
        </li>
        <li><button @click="store.logOut">로그아웃</button></li>
      </div>
      <div v-else style="display: flex; justify-content: space-between">
        <li>
          <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
        </li>
        <li><RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink></li>
      </div>
    </ul>
  </nav>

  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from "vue-router";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
</script>

<style lang="scss" scoped>
h1 {
  font-size: 2.5rem;
}
#primary_nav_wrap {
  margin-top: 15px;
  display: flex;
  justify-content: space-evenly;
}

#primary_nav_wrap ul {
  list-style: none;
  position: relative;
  float: left;
  margin: 0;
  padding: 0;
}

#primary_nav_wrap ul a,
p {
  display: block;
  color: #333;
  text-decoration: none;
  font-weight: 700;
  font-size: 12px;
  line-height: 32px;
  padding: 0 15px;
  font-family: "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

#primary_nav_wrap ul li {
  position: relative;
  float: left;
  margin: 0;
  padding: 0;
}

// #primary_nav_wrap ul li.current-menu-item {
//   background: #ddd;
// }

// #primary_nav_wrap ul li:hover {
//   background: tr;
// }

#primary_nav_wrap ul ul {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  // background: #fff;
  padding: 0;
}

#primary_nav_wrap ul ul li {
  float: none;
  width: 200px;
}

#primary_nav_wrap ul ul a {
  line-height: 120%;
  padding: 10px 15px;
}

#primary_nav_wrap ul ul ul {
  top: 0;
  left: 100%;
}

#primary_nav_wrap ul li:hover > ul {
  display: block;
}

ul > li {
  margin-left: 10px;
}

button {
  display: block;
  color: #333;
  text-decoration: none;
  font-weight: 700;
  font-size: 12px;
  line-height: 32px;
  padding: 0 15px;
  font-family: "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.logo {
  display: flex;
  justify-content: space-evenly;
}
</style>
