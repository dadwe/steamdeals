function addPrct() {
    var elems = document.getElementsByClassName("percentage");
    var length = elems.length;
    for (var i = 0; i < length; ++i) {
        elems[i].innerText += "%";
    }
}

function logOutDisplay() {
    alert("Successfully Logged Out");
}

function goLogin() {
    window.open = "login.html";
}

function count_down_chars(){
    var elem = document.getElementById("feedback");
    var count = document.getElementById("feedbackCount");
    count.innerText = 500 - elem.value.length;
    if (500 - obj.value.length < 0) {
        count.style.color = 'red';
    } else {
        count.style.color = 'black';
    }
}

function numSortUp(n) {
    var table = document.getElementById("main-table");
    var switching = true;
    while(switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i+1].getElementsByTagName("TD")[n];
            if (x.innerText < y.innerText) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function numSortDown(n) {
    var table = document.getElementById("main-table");
    var switching = true;
    while(switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i+1].getElementsByTagName("TD")[n];
            if (x.innerText > y.innerText) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function priceSortUp(n) {
    var table = document.getElementById("main-table");
    var switching = true;
    while(switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i+1].getElementsByTagName("TD")[n];
            xNum = Number(x.innerText.substring(5, x.innerHTML.length));
            yNum = Number(y.innerText.substring(5, y.innerHTML.length));
            if (xNum < yNum) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function priceSortDown(n) {
    var table = document.getElementById("main-table");
    var switching = true;
    while(switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i+1].getElementsByTagName("TD")[n];
            xNum = x.innerHTML.substring(5, x.innerHTML.length);
            yNum = y.innerHTML.substring(5, y.innerHTML.length);
            if (xNum > yNum) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function markCurrentPage() {
    pageNum = window.location.href;
    if (pageNum.includes("page")) {
        pageNum = pageNum.substr(-1 * (pageNum.length - pageNum.indexOf("=")) + 1);
    } else { //initial page loads to 1st page
        pageNum = 1;
    }

    document.getElementsByClassName("pages")[Number(pageNum) - 1].className += (" active");

}

function goTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}