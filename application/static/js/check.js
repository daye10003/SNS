$(document).ready(function(){
	$('#email').change(function(){
		if (!Boolean($(this).val().match(/^[A-Za-z0-9\._]+@[A-Za-z0-9-]+\.[(com)|(ac.kr)|(net)]*$/)))
			{$('#email_validator').show();}
		else {$('#email_validator').hide();}});
	$('#password').change(function(){
		if (!Boolean($(this).val().match(/^.*(?=.{8,20})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).*$/)))
			{$('#password_validator').show();}
		else {$('#password_validator').hide();}});
	$('#password_check').change(function(){
		if ($('#password').val() != $('#password_check').val())
			{$('#password_check_validator').show();}
		else {$('#password_check_validator').hide();}});
 });