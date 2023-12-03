<template>
  <div class="center">
    <div class="hexagon">
      <div class="hex1">
        <div class="hex2" style="background-color: #efd98f">
          <div class="desc" style="color: black">
            <h2 style="font-size: medium; font-weight: 600">
              {{ deposit.kor_co_nm }}
            </h2>
            <p>{{ deposit.fin_prdt_nm }}</p>
            <p>
              <RouterLink
                :to="{ name: 'DepositDetail', params: { id: deposit.id } }"
              >
                자세히 보기
              </RouterLink>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  deposit: Object,
});
</script>

<style lang="scss" scoped>
body {
  font-family: "Open Sans", arial, sans-serif;
  background: rgb(123, 158, 158);
}

/* 일단 2번째 */
// @import "compass/css3";

/* Thanks to dmac37 for this hex technique */

@import url(https://fonts.googleapis.com/css?family=Lato:300);

/* Variables */
$width: 220px;
$pink: rgba(230, 0, 98, 0.75);
$green: rgba(169, 160, 50, 0.75);
$yellow: rgba(252, 171, 55, 0.75);
$brown: rgba(83, 70, 54, 0.75);

// h3 {
//   font-family: "Lato", sans-serif;
//   font-size: 30px;
//   font-weight: 600;
//   text-align: center;
//   margin: 100px 10px 0 10px;
// }

// body {
//   background: #fff;
// }

// section {
//   margin: 0 auto;
//   text-align: center;
//   width: 960px;
// }

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
