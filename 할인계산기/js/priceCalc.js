function showPrice() {
  let oPrice = parseFloat(document.querySelector("#originalPrice").value);
  let rate = parseFloat(document.querySelector("#rate").value);

  if (oPrice > 0 && rate > 0) {
    let savedPrice = oPrice * (rate / 100);
    let resultPrice = oPrice - savedPrice;

    document.querySelector("#showResult").innerHTML =
      "상품의 원래 가격은 " + oPrice + "원이고," +
      "<div>할인율은 " + rate + "%입니다.</div>" +
      savedPrice.toFixed(0) + "원을 절약한 " +
      "<b>" + resultPrice.toFixed(0) + "</b>원에 살 수 있습니다.";
  } else {
    document.querySelector("#showResult").innerHTML =
      "<span style='color:red;'>가격과 할인율을 올바르게 입력하세요.</span>";
  }
}

function calcDiscountRate() {
  let original = parseFloat(document.querySelector("#originalPrice2").value);
  let final = parseFloat(document.querySelector("#finalPrice").value);

  if (original > 0 && final > 0 && final < original) {
    let rate = ((original - final) / original) * 100;

    document.querySelector("#showRateResult").innerHTML =
      "원래 가격이 " + original + "원이고, 구매 가격이 " + final + "원이므로<br>" +
      "약 <b>" + rate.toFixed(1) + "%</b> 할인되었습니다.";
  } else {
    document.querySelector("#showRateResult").innerHTML =
      "<span style='color:red;'>입력값을 다시 확인해주세요. (원래 가격 > 구매 가격이어야 함)</span>";
  }
}
