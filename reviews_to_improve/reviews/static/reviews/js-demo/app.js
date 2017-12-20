$(document).ready(function() {
  $('.progress').hide();
  $('#green-alert').hide();
  $('#blue-alert').hide();
});

$('#load').click(function() {
  $('#load').fadeOut();
  $('#blue-alert').delay(800).fadeIn().delay(8000).fadeOut();
  $('.progress').delay(800).fadeIn().delay(8000).fadeOut();
  $('#green-alert').fadeIn();
});
