// 선택시 백그라운드 색상 나타내기
function check(it) {
    charge_selection = it.parentNode.parentNode;
    charge_selection.style.backgroundColor = (it.checked) ? "#1e355f" : "white";
    charge_selection.style.color = (it.checked) ? "white" : "black";
  }
