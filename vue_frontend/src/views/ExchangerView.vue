<template>
  <div class="body">
    <h2 style="margin-bottom: 20px">환율 계산기</h2>
    <div class="currency">
      <select id="from_currency">
        <option value="AED">아랍에미리트 디르함</option>
        <option value="ARS">아르헨티나 페소</option>
        <option value="AUD">오스트레일리아 달러</option>
        <option value="BGN">불가리아 레프</option>
        <option value="BRL">브라질리안 헤알</option>
        <option value="BSD">바하마 달러</option>
        <option value="CAD">캐나디안 달러</option>
        <option value="CHF">스위스 프랑</option>
        <option value="CLP">칠레 페소</option>
        <option value="CNY">중국 위안</option>
        <option value="COP">콜롬비아 페소</option>
        <option value="CZK">체코 코루나</option>
        <option value="DKK">덴마크 크로네</option>
        <option value="DOP">도메니카 페소</option>
        <option value="EGP">이집트 파운드</option>
        <option value="EUR">유로</option>
        <option value="FJD">피지 달러</option>
        <option value="GBP">영국 파운드</option>
        <option value="GTQ">과테말라 케찰</option>
        <option value="HKD">홍콩 달러</option>
        <option value="HRK">크로아티나 쿠나</option>
        <option value="HUF">헝가리 포린트</option>
        <option value="IDR">인도네시아 루피아</option>
        <option value="ILS">이스라엘 셰켈</option>
        <option value="INR">인디안 루피</option>
        <option value="ISK">아이슬란드 크로나</option>
        <option value="JPY">일본 엔</option>
        <option value="KRW" selected>남한 원</option>
        <option value="KZT">카자흐스탄 텡게</option>
        <option value="MXN">멕시코 페소</option>
        <option value="MYR">말레이시아 링겟</option>
        <option value="NOK">노르웨이 크로네</option>
        <option value="NZD">뉴질랜드 달러</option>
        <option value="PAB">파나마 발보아</option>
        <option value="PEN">페루 솔</option>
        <option value="PHP">필리핀 페소</option>
        <option value="PKR">파키스탄 루피</option>
        <option value="PLN">폴란드 즐로티</option>
        <option value="PYG">파라과이 과라니</option>
        <option value="RON">루마니아 레우</option>
        <option value="RUB">러시아 루블</option>
        <option value="SAR">사우디 리알</option>
        <option value="SEK">스웨덴 크로나</option>
        <option value="SGD">싱가포르 달러</option>
        <option value="THB">태국 바트</option>
        <option value="TRY">터키 리라</option>
        <option value="TWD">대만 대만달러</option>
        <option value="UAH">우크라이나 흐리우냐</option>
        <option value="USD">US 달러</option>
        <option value="UYU">우루과이 페소</option>
        <option value="VND">베트남 동</option>
        <option value="ZAR">남아공 랜드</option>
      </select>
      <input type="number" id="from_ammount" placeholder="0" value="1" />
    </div>
    <div class="middle">
      <button id="exchange" style="width: 60px; height: 60px">
        <img
          src="../../assets/exchange.png"
          style="width: 40px; height: 40px"
        />
        <!-- <i class="fa-solid fa-right-left fa-rotate-90"></i> -->
      </button>
      <div class="rate" id="rate"></div>
    </div>
    <div class="currency">
      <select id="to_currency">
        <option value="AED">아랍에미리트 디르함</option>
        <option value="ARS">아르헨티나 페소</option>
        <option value="AUD">오스트레일리아 달러</option>
        <option value="BGN">불가리아 레프</option>
        <option value="BRL">브라질리안 헤알</option>
        <option value="BSD">바하마 달러</option>
        <option value="CAD">캐나디안 달러</option>
        <option value="CHF">스위스 프랑</option>
        <option value="CLP">칠레 페소</option>
        <option value="CNY">중국 위안</option>
        <option value="COP">콜롬비아 페소</option>
        <option value="CZK">체코 코루나</option>
        <option value="DKK">덴마크 크로네</option>
        <option value="DOP">도메니카 페소</option>
        <option value="EGP">이집트 파운드</option>
        <option value="EUR">유로</option>
        <option value="FJD">피지 달러</option>
        <option value="GBP">영국 파운드</option>
        <option value="GTQ">과테말라 케찰</option>
        <option value="HKD">홍콩 달러</option>
        <option value="HRK">크로아티나 쿠나</option>
        <option value="HUF">헝가리 포린트</option>
        <option value="IDR">인도네시아 루피아</option>
        <option value="ILS">이스라엘 셰켈</option>
        <option value="INR">인디안 루피</option>
        <option value="ISK">아이슬란드 크로나</option>
        <option value="JPY">일본 엔</option>
        <option value="KRW">남한 원</option>
        <option value="KZT">카자흐스탄 텡게</option>
        <option value="MXN">멕시코 페소</option>
        <option value="MYR">말레이시아 링겟</option>
        <option value="NOK">노르웨이 크로네</option>
        <option value="NZD">뉴질랜드 달러</option>
        <option value="PAB">파나마 발보아</option>
        <option value="PEN">페루 솔</option>
        <option value="PHP">필리핀 페소</option>
        <option value="PKR">파키스탄 루피</option>
        <option value="PLN">폴란드 즐로티</option>
        <option value="PYG">파라과이 과라니</option>
        <option value="RON">루마니아 레우</option>
        <option value="RUB">러시아 루블</option>
        <option value="SAR">사우디 리알</option>
        <option value="SEK">스웨덴 크로나</option>
        <option value="SGD">싱가포르 달러</option>
        <option value="THB">태국 바트</option>
        <option value="TRY">터키 리라</option>
        <option value="TWD">대만 대만달러</option>
        <option value="UAH">우크라이나 흐리우냐</option>
        <option value="USD" selected>US 달러</option>
        <option value="UYU">우루과이 페소</option>
        <option value="VND">베트남 동</option>
        <option value="ZAR">남아공 랜드</option>
      </select>
      <input type="number" id="to_ammount" placeholder="0" />
    </div>
  </div>
</template>

<script setup>
if (typeof document != "undefined") {
  setTimeout(() => {
    const from_currencyEl = document.getElementById("from_currency");
    const from_ammountEl = document.getElementById("from_ammount");
    const to_currencyEl = document.getElementById("to_currency");
    const to_ammountEl = document.getElementById("to_ammount");
    const rateEl = document.getElementById("rate");
    const exchange = document.getElementById("exchange");

    from_currencyEl.addEventListener("change", calculate);
    from_ammountEl.addEventListener("input", calculate);
    to_currencyEl.addEventListener("change", calculate);
    to_ammountEl.addEventListener("input", calculate);

    exchange.addEventListener("click", () => {
      const temp = from_currencyEl.value;
      from_currencyEl.value = to_currencyEl.value;
      to_currencyEl.value = temp;
      calculate();
    });

    function calculate() {
      const from_currency = from_currencyEl.value;
      const to_currency = to_currencyEl.value;

      fetch(`https://api.exchangerate-api.com/v4/latest/${from_currency}`)
        .then((res) => res.json())
        .then((res) => {
          const rate = res.rates[to_currency];
          rateEl.innerText = `1 ${from_currency} = ${rate} ${to_currency}`;
          to_ammountEl.value = (from_ammountEl.value * rate).toFixed(2);
        });
    }

    calculate();
  }, 500);
}
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Muli&display=swap");
.body {
  margin-top: 15%;
  border: 1px solid rgb(189, 189, 189);
  padding: 1rem;
}
* {
  box-sizing: border-box;
  width: 80%;
  margin: auto;
}

body {
  background-image: linear-gradient(
    to bottom,
    #fff 0%,
    #fff 50%,
    #ecf0f1 50%,
    #f1f2f6 100%
  );
  font-family: "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.currency {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.currency select {
  background: transparent;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%20000002%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
  background-repeat: no-repeat, repeat;
  background-position: right 0.2em top 50%, 0 0;
  background-size: 0.5em auto, 100%;
  border: 0;
  padding-right: 20px;
  font-size: 15px;
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
}

.currency input {
  border: 0;
  background: transparent;
  font-size: 15px;
  text-align: right;
}

.middle {
  color: rgb(0, 117, 235);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.middle button {
  background-color: #fff;
  border: 2px solid #ecf0f1;
  border-radius: 50%;
  cursor: pointer;
  color: rgb(0, 117, 235);
  font-size: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 30px;
  width: 30px;
  transform: rotate(90deg);
}

.middle button:active {
  transform: rotate(90deg) scale(0.9);
}

.middle .rate {
  background-color: #fff;
  border: 2px solid #ecf0f1;
  border-radius: 50px;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 30px;
  padding: 0 10px;
  margin: 30px 15px 30px 25px;
}

select:focus,
input:focus,
button:focus {
  outline: 0;
}

/* SOCIAL PANEL CSS */
.social-panel-container {
  position: fixed;
  right: 0;
  bottom: 80px;
  transform: translateX(100%);
  transition: transform 0.4s ease-in-out;
}

.social-panel-container.visible {
  transform: translateX(-10px);
}

.social-panel {
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 16px 31px -17px rgba(0, 31, 97, 0.6);
  border: 5px solid #001f61;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: "Muli";
  position: relative;
  height: 169px;
  width: 370px;
  max-width: calc(100% - 10px);
}

.social-panel button.close-btn {
  border: 0;
  color: #97a5ce;
  cursor: pointer;
  font-size: 20px;
  position: absolute;
  top: 5px;
  right: 5px;
}

.social-panel button.close-btn:focus {
  outline: none;
}

.social-panel p {
  background-color: #001f61;
  border-radius: 0 0 10px 10px;
  color: #fff;
  font-size: 14px;
  line-height: 18px;
  padding: 2px 17px 6px;
  position: absolute;
  top: 0;
  left: 50%;
  margin: 0;
  transform: translateX(-50%);
  text-align: center;
  width: 235px;
}

.social-panel p i {
  margin: 0 5px;
}

.social-panel p a {
  color: #ff7500;
  text-decoration: none;
}

.social-panel h4 {
  margin: 20px 0;
  color: #97a5ce;
  font-family: "Muli";
  font-size: 14px;
  line-height: 18px;
  text-transform: uppercase;
}

.social-panel ul {
  display: flex;
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.social-panel ul li {
  margin: 0 10px;
}

.social-panel ul li a {
  border: 1px solid #dce1f2;
  border-radius: 50%;
  color: #001f61;
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  width: 50px;
  text-decoration: none;
}

.social-panel ul li a:hover {
  border-color: #ff6a00;
  box-shadow: 0 9px 12px -9px #ff6a00;
}

.floating-btn {
  border-radius: 26.5px;
  background-color: #001f61;
  border: 1px solid #001f61;
  box-shadow: 0 16px 22px -17px #03153b;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
  line-height: 20px;
  padding: 12px 20px;
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 999;
}

.floating-btn:hover {
  background-color: #ffffff;
  color: #001f61;
}

.floating-btn:focus {
  outline: none;
}

.floating-text {
  background-color: #001f61;
  border-radius: 10px 10px 0 0;
  color: #fff;
  font-family: "Muli";
  padding: 7px 15px;
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  z-index: 998;
}

.floating-text a {
  color: #ff7500;
  text-decoration: none;
}

@media screen and (max-width: 480px) {
  .social-panel-container.visible {
    transform: translateX(0px);
  }

  .floating-btn {
    right: 10px;
  }
}
</style>
