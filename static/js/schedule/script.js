function redirectToSchedual() {
    // 在這裡指定跳轉的網址
    window.location.href = 'select.html';
}

function addNewRow() {
    var tbody = document.getElementById('sortable-table');
    var rowCount = tbody.getElementsByTagName('tr').length;
    var newRow = document.createElement('tr');
    newRow.innerHTML =  '<td><img src="img/schedual.png" alt="行程圖示" class="schedual-icon" /></td>' +
                        '<td contenteditable="true" class="editable-text">行程' + (rowCount + 1) + '</td>' +
                        '<td>' +
                        '<button class="btn btn-primary view-btn" onclick="redirectToSchedual()">查看</button>' +
                        '<button class="btn btn-danger delete-btn" onclick="deleteRow(this); renumberRows();">刪除</button>' +
                        '</td>';
    tbody.appendChild(newRow);
    renumberRows(); // 新增行程後重新編號
}

function deleteRow(button) {
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

function renumberRows() {
    var tbody = document.getElementById('sortable-table');
    var rows = tbody.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var nameCell = rows[i].getElementsByTagName('td')[1];
        var currentName = nameCell.textContent;

        // 檢查行程名稱是否符合格式 "行程+數字"
        var pattern = /^行程(\d+)$/; // 正則表達式，匹配 "行程+數字" 格式
        var match = currentName.match(pattern);

        if (match) {
            // 提取匹配到的數字，並重新編號
            var newNumber = i + 1;
            var newName = '行程' + newNumber;
            nameCell.textContent = newName;
        }
        // 如果行程名稱不符合格式，則不進行重新編號
    }
}
