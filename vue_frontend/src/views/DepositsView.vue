<template>
  <section>
    <div class="hex_row_odd">
      <DepositItem
        v-for="deposit in store.deposits.slice(0, 3)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <!--/hex_row_even-->
    <div class="hex_row_even">
      <DepositItem
        v-for="deposit in store.deposits.slice(3, 7)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_odd">
      <DepositItem
        v-for="deposit in store.deposits.slice(7, 10)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_even">
      <DepositItem
        v-for="deposit in store.deposits.slice(10, 14)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_odd">
      <DepositItem
        v-for="deposit in store.deposits.slice(14, 17)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_even">
      <DepositItem
        v-for="deposit in store.deposits.slice(17, 21)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_odd">
      <DepositItem
        v-for="deposit in store.deposits.slice(21, 24)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_even">
      <DepositItem
        v-for="deposit in store.deposits.slice(24, 28)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_odd">
      <DepositItem
        v-for="deposit in store.deposits.slice(28, 31)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_even">
      <DepositItem
        v-for="deposit in store.deposits.slice(31, 35)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
    <div class="hex_row_odd">
      <DepositItem
        v-for="deposit in store.deposits.slice(35)"
        :key="deposit"
        :deposit="deposit"
      ></DepositItem>
    </div>
  </section>
</template>

<script setup>
import { useCounterStore } from "@/stores/product";
import DepositItem from "@/components/DepositItem.vue";

const store = useCounterStore();

document.addEventListener("hover", function () {
  var color = "one";
  var counter = 0;
  var desc = document.querySelector(".desc");
  var hexagon = document.querySelector(".hexagon");
  desc.hide();
  hexagon.hover(
    function () {
      this.find(".desc").fadeIn("fast");
      counter++;
      if (counter === 0) {
        color = "base";
      } else if (counter === 1) {
        color = "one";
      } else if (counter === 2) {
        color = "two";
      } else if (counter === 3) {
        color = "three";
      } else if (counter >= 4) {
        counter = 0;
        color = "base";
      }
      this.find(".desc").addClass(color);
    },
    function () {
      this.find(".desc").fadeOut("fast", function () {
        this.removeClass(color);
      });
    }
  );
});
</script>

<style lang="scss" scoped>
/* 일단 2번째 */

@import url(https://fonts.googleapis.com/css?family=Lato:300);

/* Variables */
$width: 220px;
$pink: rgba(230, 0, 98, 0.75);
$green: rgba(169, 160, 50, 0.75);
$yellow: rgba(252, 171, 55, 0.75);
$brown: rgba(83, 70, 54, 0.75);

h3 {
  font-family: "Lato", sans-serif;
  font-size: 30px;
  font-weight: 600;
  text-align: center;
  margin: 100px 10px 0 10px;
}

body {
  background: #fff;
}

section {
  margin: 1rem auto 0 auto;
  text-align: center;
  width: 960px;
}

.hex_row_even {
  display: inline-block;
  margin: 0 0 -275px 0;
  overflow: hidden;
}

.hex_row_odd {
  display: inline-block;
  margin: 0 0 -275px 0;
  overflow: hidden;
}

.center {
  float: left;
  margin: 15px 5px;
  width: $width;
}

.hexagon {
  transform: rotate(120deg);
  cursor: pointer;
  height: ($width * 2);
  overflow: hidden;
  visibility: hidden;
  width: $width;
}

.hex1 {
  transform: rotate(-60deg);
  height: 100%;
  overflow: hidden;
  width: 100%;
}

.hex2 {
  transform: rotate(-60deg);
  height: 100%;
  position: relative;
  visibility: visible;
  width: 100%;
  &[style] {
    background-size: cover !important;
  }
}

.desc {
  color: white;
  font-family: "Lato", sans-serif;
  font-size: 1.5em;
  font-weight: 300;
  height: ($width * 2);
  line-height: 1.5em;
  position: absolute;
  text-align: center;
  text-transform: uppercase;
  visibility: visible;
  width: $width;
  &.base {
    background: $pink;
  }
  &.one {
    background: $yellow;
  }
  &.two {
    background: $green;
  }
  &.three {
    background: $brown;
  }
  h2 {
    margin: ($width - ($width / 4)) 20px 0 20px;
  }
  p {
    font-size: 0.5em;
    text-transform: lowercase;
  }
}
</style>
