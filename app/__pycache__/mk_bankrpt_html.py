def mk_bankrpt_html():
	welcome="""
			<!DOCTYPE html>
<html>
<head>
  <title>Aggregated Banking Activity</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container-fluid">
	<iframe height="640" width="320" frameborder="0" scrolling="no" src="//plot.ly/~jdey123/4.embed"></iframe>
</div>

</body>
</html>
			"""
	return welcome
