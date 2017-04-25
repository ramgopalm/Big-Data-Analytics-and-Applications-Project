$(function () {

  // sorce: http://stackoverflow.com/a/22172860
  function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);
    var dataURL = canvas.toDataURL("image/jpeg");

    return dataURL.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
  }

  $('.thumbnail img')
    .click(function () {
      var btm_img = $(this).attr('src');
      $('#img_plc').attr('src', btm_img);
    });

  $("#clk").on('click', function (event) {
    $('#txt_area').hide();
    $('#meow').show();
    console.log('after meow')
    //var tmp_img = document.createElement("img");
    //console.log(tmp_img)
    //tmp_img.src = 'http://'+location.host+$('#img_plc').attr('src');
    //var base64 = getBase64Image(tmp_img);
    //console.log(base64)

      var ip1 = document.getElementById('ip1').value;
      var ip2 = document.getElementById('ip2').value;
      var ip3 = document.getElementById('ip3').value;
      var ip4 = document.getElementById('ip4').value;
      var ip5 = document.getElementById('ip5').value;
      var ip6 = document.getElementById('ip6').value;
      var ip7 = document.getElementById('ip7').value;
      var ip8 = document.getElementById('ip8').value;
      var ip9 = document.getElementById('ip9').value;
      var ip10 = document.getElementById('ip10').value;
      var ip11 = document.getElementById('ip11').value;
      var ip12 = document.getElementById('ip12').value;
      var ip13 = document.getElementById('ip13').value;


    $.ajax({
      type: "POST",
      url: "http://localhost:5000/api/predict",
      data: { value1: ip1,value2: ip2,value3: ip3,value4: ip4,value5: ip5,value6: ip6,value7: ip7,value8: ip8,value9: ip9,value10: ip10,value11: ip11,value12: ip12,value13: ip13 },
      success: function (result) {
       // var res = result[0];
          var res = result.results[0];
          console.log(res)
          console.log(result.results[0])
        $('#meow').hide();
        $('#txt_area').text(res[0]);
        $('#txt_area').show();
      }
    });
  });
});
