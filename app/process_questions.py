def process_questions(form_data):
	from qry_pca_json_msgs import qry_pca_json_msgs
	welcome="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">

    <title>Best PCA Results</title>
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
  width: 100%
}

.table-fixed td {
   min-height: 300px
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
                <h1>Your results</h1>
                <p>Your results are based on the following criteria that you selected:-
	<br>Age:
"""
	welcome=welcome+str(form_data['age'])
	welcome=welcome+"<br>Residency:"
	welcome=welcome+str(form_data['residency'])
	welcome=welcome+"<br>Student/Graduate?:"
	welcome=welcome+str(form_data['academic'])
	welcome=welcome+"<br>Typical days overdrawn each month:"
	welcome=welcome+str(form_data['daysoverdrawn'])
	welcome=welcome+"<br>Do you have an arranged overdraft?:"
	welcome=welcome+str(form_data['arrangedoverdraft'])
	if 'overdraftlimit' in form_data:
		welcome=welcome+"<br>Current overdraft limit:"
		welcome=welcome+str(form_data['overdraftlimit'])

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
	welcome=welcome+qry_pca_json_msgs('General')
	welcome=welcome+"\n</tbody>\n</table>\n</div>\n</body>\n</html>"

	return welcome
