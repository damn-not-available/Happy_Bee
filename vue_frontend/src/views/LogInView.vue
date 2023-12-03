<template>
  <div class="vid-container" style="margin-top: 10%">
    <div class="box">
      <h1>Login</h1>
      <form @submit.prevent="logIn">
        <input type="text" placeholder="Username" v-model.trim="username" />
        <input type="password" placeholder="Password" v-model.trim="password" />
        <button type="submit">Login</button>
      </form>
      <p>
        회원이 아니신가요?
        <span
          ><RouterLink :to="{ name: 'SignUpView' }">Sign Up</RouterLink></span
        >
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password = ref(null);
const isLoginFailed = store.isLoginFailed;

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style lang="scss" scoped>
body {
  padding: 0;
  margin: 0;
}
.vid-container {
  position: relative;
  height: 100vh;
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
  background: rgba(0, 0, 0, 0);
  padding: 30px 0px;
}
.box h1 {
  text-align: center;
  margin: 30px 0;
  font-size: 30px;
}
.box input {
  display: block;
  width: 300px;
  margin: 20px auto;
  padding: 15px;
  background: rgba(172, 130, 15, 0.2);
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
