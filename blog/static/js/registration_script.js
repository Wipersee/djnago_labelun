function validate(){
	var userEmail = document.getElementById('user_email');
	var userPassword = document.getElementById('id_password1');
	var emailMatch = /^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))@([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$/;
	var userName = document.getElementById('user_name');
	var error = document.getElementById('invalid');
	var error_inner = document.getElementById('invalid_p');
	if(!userName.value || userName.value.trim() == ' '){
		userName.style.border = "1px solid red";
		error_inner.innerHTML = 'Invalid Name';
		error.style.display = 'block';
		error.setAttribute('class','active');
		setTimeout(() => error.setAttribute('class','hidden'),2000);
		setTimeout(() => error.style.display='none',3000);
		return false;
	}
	if(!userPassword.value || userPassword.value.length < 6){
		userPassword.style.border = '1px solid red';
		error_inner.innerHTML = 'Invalid Password(min 6 chars)';
		error.style.display = 'block';
		error.style.width="13rem";
		error.setAttribute('class','active');
		setTimeout(() => error.setAttribute('class','hidden'),2000);
		setTimeout(() => error.style.display='none',3000);
		return false;
	}
	if(!userEmail.value || userEmail.value.match(emailMatch) == null){
		userEmail.style.border = '1px solid red';
		error_inner.innerHTML = 'Invalid Email';
		error.style.display = 'block';
		error.style.width="7rem";
		error.setAttribute('class','active');
		setTimeout(() => error.setAttribute('class','hidden'),2000);
		setTimeout(() => error.style.display='none',3000);
		return false;
	}
	return true;
}