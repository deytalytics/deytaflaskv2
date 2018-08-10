def process_bca_questions(form_data):
	from app.qry_bca_json_msgs import qry_bca_json_msgs
	welcome="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex, nofollow">

    <title>Best BCA Results</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <style type="text/css">
	
	img {
    border: 1px solid #ddd;
    width: 50px;
	min-height: 50px
}

.table-fixed thead {
  width: 98%
  }
  
.table-fixed th {
 background-color: #DFDFDF
}
.table-fixed tbody {
  height: 580px;
  overflow-y: auto;
  width: 100%;
}

.table-fixed td {
   min-height: 200px
   }
   
.table-fixed thead, .table-fixed tbody, .table-fixed tr, .table-fixed td, .table-fixed th {
  display: block;
}

.table-fixed tbody td, .table-fixed thead > tr> th {
  float: left;
}
    </style>
    <script src="//code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
</head>
<body>
	<div class="container">
	<div class="row">
		<h1>Your results</h1>
		<p>Your results are based on the following criteria that you selected:-
		<br><b>Account type: </b>
	"""
	
	bcastr=form_data['bca'].upper()
	
	if bcastr=="SWITCH":
		welcome=welcome+"Switcher"
	elif bcastr=="STARTUP":
		welcome=welcome+"Startup"
	elif bcastr=="ESTABLISHED":
		welcome=welcome+"Standard"
	elif bcastr=="NONCOMM":
		welcome=welcome+"Charities, Clubs & Societies"

	welcome=welcome+"""
  		</p>
				<table class="table table-fixed">
					<thead>
						<tr>
							<th class="col-xs-4">Product</th>
							<th class="col-xs-4">Credit Interest</th>
							<th class="col-xs-4">Overdraft</th>
						</tr>
					</thead>
					<tbody>
	"""

	welcome=welcome+qry_bca_json_msgs(bcastr)
		
	welcome=welcome+"</tbody></table></div></div></body></html>"
	return welcome
