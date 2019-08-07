	jQuery(document).ready(function($) {
		
	//lightcase initiator
	
		$('a[data-rel^=lightcase]').lightcase({
		    
		    closeOnOverlayClick: false,
		   
		   
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





