$(document).ready(function() {
  $('.progress').hide();
});

$('#load').click(function() {
  $('#load').fadeOut();
  $('.progress').delay(800).fadeIn();
});

// setTimeout(function() {
//   $this.button('reset');
// }, 8000);
