document.addEventListener('DOMContentLoaded', function () {
  // 获取表格的tbody部分
  var tableBody = document.querySelector('tbody');

  // 初始化Sortable
  var sortable = new Sortable(tableBody, {
    animation: 150,
    handle: 'th, td', // 设置哪个部分可以拖动
    onEnd: function (evt) {
      // 当拖动结束时触发的回调
      updateRowNumbers();
    },
  });

  // 更新每一行的序号
  function updateRowNumbers() {
    var rows = tableBody.querySelectorAll('tr');
    rows.forEach(function (row, index) {
      // 更新每一行的序号
      var rowNumberCell = row.querySelector('th[scope="row"]');
      if (rowNumberCell) {
        rowNumberCell.textContent = index + 1;
      }
    });
  }

  // 绑定删除按钮的点击事件
  tableBody.addEventListener('click', function (event) {
    if (event.target.tagName === 'BUTTON' && event.target.classList.contains('btn-danger')) {
      // 如果点击的是删除按钮
      var rowToRemove = event.target.closest('tr');
      if (rowToRemove) {
        rowToRemove.remove();
        updateRowNumbers(); // 删除后更新序号
      }
    }
  });
});

  // 绑定保存按钮的点击事件
  document.getElementById("saveToDBButton").addEventListener("click", function() {
    window.location.href = "index.html";
  });