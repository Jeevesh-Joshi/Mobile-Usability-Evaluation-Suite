console.log("here");
var buttonRecord = document.getElementById("record");
var buttonStop = document.getElementById("stop");
var downloadLink = document.getElementById("download");
downloadLink.style.display = "none";

buttonStop.disabled = true;

buttonRecord.onclick = function(event) {
    event.preventDefault();
    console.log("start");
    // var url = window.location.href + "record_status";
    buttonRecord.disabled = true;
    buttonStop.disabled = false;
    
    // disable download link
    
    downloadLink.text = "";
    downloadLink.href = "";

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "true" }));
};

buttonStop.onclick = function() {
    console.log("stop");
    downloadLink.style.display = "inline";

    buttonRecord.disabled = false;
    buttonStop.disabled = true;    

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);

            // enable download link
            downloadLink.text = "Save";
            downloadLink.href = "/static/video.avi";
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false" }));
};

downloadLink.onclick = function () {
    downloadLink.style.display = "none";
}