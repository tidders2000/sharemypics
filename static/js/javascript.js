	jQuery(document).ready(function($) {
		
	//lightcase initiator
	
		$('a[data-rel^=lightcase]').lightcase({
		    
		    closeOnOverlayClick: false,
		   
		   
		});
	// disable right click
		$(document).bind("contextmenu",function(e){
    return false;
});
	
	
	

	});





