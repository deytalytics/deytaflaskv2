def mk_bca_questionnaire():
	welcome="""
			<html>
<head>
  <title>Business Current Account Questionnaire</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js"></script>
</head>
			<body> 
				<style>
					{  
						background: no-repeat center center fixed url("ukmoney.jpg");
						background-size: cover;  
						background-color: #cccccc;
					}
				</style>
				<div class="container-fluid">
					<h1>Business Current Account Questionnaire</h1>
					In order to provide you with the best personal current account products, we'd be grateful if you would be able to complete the following questions
					<br>
					<form action="process_bca_questions" name="bca_questionnaire" method="POST">
						What type of business account would you like?
						<select name="bca">
							<option value="startup">Startup</option>
							<option value="switch">Switcher</option>
							<option value="established">Standard</option>
							<option value="noncomm">Charities, Clubs & Societies</option>
						</select><br><br>
						<input type="submit" value="Submit">
					</form>
				</div>
			</body>
			</html>
			"""
	return welcome
