$(document).ready(function() {
  $('.progress').hide();
});

$('#load').on('click', function() {
  var $btn = $('#load');
  $btn.hide();
  $('.progress').show();
  // setTimeout(function() {
  //   $this.button('reset');
  // }, 8000);
});
