
// 전체선택 기능 구현하기
function selectAll(selectAll)  {
    const checkboxes 
         = document.getElementsByName('lecture');
    
    checkboxes.forEach((checkbox) => {
      checkbox.checked = selectAll.checked;
    })
  }