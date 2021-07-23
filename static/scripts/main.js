// funtion to check the password strength
$(() => {
	$('#password1').blur(()=>{

		// display the password strength span
		$('.displayBadge').css('display', 'block')

		let passwordVal = $('#password1')
		// checking password length
		if(passwordVal.val().length < 8){
			console.log(passwordVal.val())
			$('#password-para-chars').fadeIn('fast')
			// displaying the block with strength estimation
			$('.displayBadge').css('background-color', 'red')
			$('.displayBadge').text('Weak')
		} else{
			// password length more than 8
			passwordVal = passwordVal.val()
			console.log(passwordVal)

			// display none if the password length is more than 8
			$('#password-para-chars').css('display','none')
			$('.displayBadge').css('background-color', 'lightblue')
			// badge text set to medium strength
			$('.displayBadge').text('Medium') 
			// checking for password having a number
			if(/[0-9]/.test(passwordVal)){
				$('progress').attr('value', 75)
				console.log(passwordVal)
				// checking for password having a special charachter
				if( /[!@#$%^&*.]/.test(passwordVal) ){
					console.log(passwordVal)

					$('.displayBadge').css('background-color', 'lightgreen')
					$('.displayBadge').text('Strong')
					$('#password-para-spl').css('display','none')
					let btnsubmit = $('#btnsubmitregister');
					console.log('on btn')
					// if all the conditions check out only then the 
					// submit button will have the property submit set to 
					// enabled
					btnsubmit.prop('disabled', false);

				} else {
					$('#password-para-num').css('display','none')
					$('#password-para-spl').fadeIn()
					
				}
			} else {
				$('#password-para-num').fadeIn()
			}
		}
	})
})