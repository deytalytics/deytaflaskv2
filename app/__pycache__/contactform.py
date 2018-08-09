def contactform():
	welcome="""
			<html>
				<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
				<title>Contact Us</title>
				<link rel='stylesheet' id='contact-form-css'  href='static/contactform.css' type='text/css' media='all' />
			</head>
			<body>


<form action="/postcontact" method="post" class="wpcf7-form" novalidate="novalidate">
<p>Your Name (required)<br />
    <span class="your-name"><input type="text" name="your-name" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" aria-required="true" aria-invalid="false" /></span> </p>
<p>Your Email (required)<br />
    <span class="your-email"><input type="email" name="your-email" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email" aria-required="true" aria-invalid="false" /></span> </p>
<p>Subject<br />
    <span class="your-subject"><input type="text" name="your-subject" value="" size="40" class="wpcf7-form-control wpcf7-text" aria-invalid="false" /></span> </p>
<p>Your Message<br />
    <span class="your-message"><textarea name="your-message" cols="40" rows="10" class="wpcf7-form-control wpcf7-textarea" aria-invalid="false"></textarea></span> </p>
<p><input type="submit" value="Send" class="wpcf7-form-control wpcf7-submit" /></p>
</form>
			</body>
			</html>
			"""
	return welcome
