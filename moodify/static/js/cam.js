  var video = document.getElementById("videoElement");
  var canvas = document.getElementById('canvas');
  var context=canvas.getContext('2d');


if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: true})
  .then(function(stream) {
    video.srcObject = stream;
  })
  .catch(function(err0r) {
    console.log("Something went wrong!");
  });
}

function snap() {
    context.fillRect(0,0,320,240);
    context.drawImage(video,0,0,320,240);
    var image = canvas.toDataURL("image/png");  // base64-encoded image using canvas.toDataURL
    var arr = image.split(",",2); // remove metadata
    var img64 = arr[1];
    $.ajax({
            contentType: 'application/json;charset=UTF-8',
            url: '/test',
            type: 'POST',
            data: JSON.stringify({img64}),
            success: function (result) {
            },
            error: function (result) {
            }
        });   //end ajax
  }



