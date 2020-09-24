$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const URL = 'https://fourtonfish.com/hellosalut/?lang=';
    const lc = $('INPUT#language_code').val();
    $.get(URL + lc , function (data) 
      $('DIV#hello').html(data.hello);
    });
  });
});
