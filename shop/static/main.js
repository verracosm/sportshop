$(document).ready(function() {
	$(document).on('click', '.clear-basket-button', function() {
		setTimeout(function(){
 		 window.location.reload();
		});
	});
	$(document).on('click', '.add-order-button', function() {
		setTimeout(function(){
 		 window.location.reload();
		});
	});
	$(document).on('click', '.pay-order-button', function() {
		alert('Zapłać mordezcczka tu - 293492 928349 2984 298429849 823');
	});
	$(document).on('click', '.add-to-basket-button', function(){
	    element = $(this);

	    $.ajax({
	      url: $(this).data('url'),
	      type: 'GET',
	      dataType: 'json',

	      beforeSend: function() {
	        
	      },
	      success: function(data) {
	      	if (data.empty == false) {
	      		element.addClass('added');
	      		element.text('Dodano!');
	      		setTimeout(function() {
				    element.text('Dodaj do koszyka');
	      			element.removeClass('added');
				  }, 400);
	      	} else {
	      		element.addClass('not-added');
	      		element.text('Brak produktu w magazynie :(');
	      	}
	      }
  		});
	});
});