function checkSelection(element) {
  if (element.value != "") {
    element.style.borderColor = "green"; //change color to green
  }
}

$(document).ready(function () {
  // Handle Predicted Result
  $("#result").ready(function () {
    // Handling the predited result to be green in case of ** Death occured**
    if ($("#result").text() == "Death occured") {
      document.getElementById("result").innerHTML =
        '<h1 id="result"><strong> Death occured </strong></h1> ';
      $("#result").css("color", "green");
      document.getElementById("result").style.display = "block";
    }

    // Handling the predited result to be red in case of ** Death not occured **
    if ($("#result").text() == "Death not occured") {
      document.getElementById("result").innerHTML =
        '<h1 id="result"><strong> Death not occured </strong></h1>';
      $("#result").css("color", "#f22849");
      document.getElementById("result").style.display = "block";
    }
  });
});

$(function () {
  $("#calculateButton").click(function () {
    console.log("clicked");
    if (document.getElementById("result").innerText) {
      $("#resultmodal").modal("show");
    }
  });
});
