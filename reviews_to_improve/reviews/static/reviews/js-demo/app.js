$(document).ready(function() {
  $('.progress').hide();
});

$('.btn').on('click', function() {
  var $this = $(this);
  $this.hide();
  $('.progress').show();
  setTimeout(function() {
    $this.button('reset');
  }, 8000);
});
