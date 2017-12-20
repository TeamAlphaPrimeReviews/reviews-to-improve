$(document).ready(function() {
  $('.progress').hide();
});

$('#load').click(function() {
  $('#load').fadeOut();
  $('.progress').delay(800).fadeIn().delay(8000).fadeOut();
  $('.alert alert-success').fadeIn();
});
