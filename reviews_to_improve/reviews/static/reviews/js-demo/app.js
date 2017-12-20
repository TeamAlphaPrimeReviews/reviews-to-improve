$(document).ready(function() {
  $('.progress').hide();
});

$('#load').on('click', function() {
  $('#load').fadeOut();
  $('.progress').fadeIn();
});

// setTimeout(function() {
//   $this.button('reset');
// }, 8000);
