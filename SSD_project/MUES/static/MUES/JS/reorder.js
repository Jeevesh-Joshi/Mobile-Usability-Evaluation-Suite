console.log("here");
var buttonRecord = document.getElementById("record");
var buttonStop = document.getElementById("stop");
var downloadLink = document.getElementById("download");
var recDetails = document.getElementById("recDetails");
var uname = document.getElementById("uname");
var uname = document.getElementById("uname");
var utasks = document.getElementById("utasks");
var token1;
var token2;
downloadLink.style.display = "none";

buttonStop.disabled = true;

buttonRecord.onclick = function(event){
    event.preventDefault();
    console.log("start");
    token1 = uname.options[uname.selectedIndex].getAttribute("data-uname");
    token2 = utasks.options[utasks.selectedIndex].getAttribute("data-tname");
    video_name = token1+"_"+token2;
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
    xhr.send(JSON.stringify({ status: "true", vname:video_name}));
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
            video_name = token1+"_"+token2;
            downloadLink.innerHTML = "Save";
            // downloadLink.href = "/static/video_name.mp4";
            downloadLink.href = `MUES/static/Recordings/${video_name}.mp4`;
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false", uid:uname.value, tid:utasks.value, vname:video_name}));
};

downloadLink.onclick = function (e) {
    downloadLink.style.display = "none";
}