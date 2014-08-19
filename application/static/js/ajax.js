$(document).ready(function(){
	$('#email').change(function(){
		var email = $('#email').val();
		$.ajax({
			url : '/email_check',
			type : 'POST',
			data : {"email" : email},
			success : function(response){
				var result = $.parseJSON(response);
				if ('message' in result){
					$('#email_check').show();}
				else{$('#email_check').hide();}
			},
			error : function(){
				console.log('error');
			},
			complete : function(){
				console.log('complete')
			},
		});
	});
});