$(document).ready(function(){
    $('#phone').mask('+7(000)000-00-00');

    $('#contactForm').on('submit', function(event){
      event.preventDefault();
      $('#contactForm').hide();
      $('#successMessage').show();
    });
  });