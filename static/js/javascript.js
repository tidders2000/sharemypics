	jQuery(document).ready(function($) {
	  
	  $('.toast').toast()
		
$("a#single_image").fancybox();
	
	/* Using custom settings */
	
	$("a#inline").fancybox({
		'hideOnContentClick': true
	});

	/* Apply fancybox to multiple items */
	
	$("a.group").fancybox({
		'transitionIn'	:	'elastic',
		'transitionOut'	:	'elastic',
		'speedIn'		:	600, 
		'speedOut'		:	200, 
		'overlayShow'	:	false
	});
	

	// disable right click
		$(document).bind("contextmenu",function(e){
    return false;
});
	
	
$(function() {
	
  //initialise form to stop 0 quantity being entered by user
  
  $("#quantity_form").validate({
    //  validation rule
    rules: {
      
      quantity:{
      	required: true,
        min: 1
      },
     
     
    
    },
    // error message
    messages: {
      quantity: "Must be greater than 0",
      
    },
    errorElement: 'div',
    errorLabelContainer: '.errortxt',
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});	

	});





