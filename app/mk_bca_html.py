def mk_bca_html():
	from qry_bca_json_msgs import qry_bca_json_msgs

	welcome = """
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	  <title>Business Current Account Price Comparison</title>
	  <link  rel="stylesheet" type="text/css" href="./static/tabs.css">
	  <link  rel="stylesheet" type="text/css" href="./static/scrolltable.css">
	</head>
	<body>
	  <p><style="color:red">Check out <a href="./static/newukcompanies.html">how many companies have incorporated in the UK each month in 2017</a>
	  <ul class="tabs">
	"""

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab1" />
        <label for="tab1">Startup</label>
        <div id="tab-content1" class="content">
		<h1>Startup Business Bank Account</h1>
		<p>Typically provides a fee-free promotional period for newly established companies</p>
  		<table class="fixed_headers">
  		<thead>
    			<tr>
      				<th>Brand</th>
      				<th>Product Information</th>
      				<th>Credit Interest</th>
                                <th>Borrowing/Overdraft</th>
    			</tr>
  		</thead>
  		<tbody>
	"""
	welcome=welcome+qry_bca_json_msgs('START UP')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab2" />
        <label for="tab2">Switcher</label>
        <div id="tab-content2" class="content">
                <h1>Business Switcher Account</h1>
                <p>Typically offers a fee-free promotional period for established companies who willing to switch their main bank account</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Credit Interest</th>
                                <th>Borrowing/Overdraft</th>
                        </tr>
                </thead>
                <tbody>
	"""
	welcome=welcome+qry_bca_json_msgs('SWITCHER')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" checked="checked" name="tabs" id="tab3" />
        <label for="tab3">Standard</label>
        <div id="tab-content3" class="content">
                <h1>Standard Business Bank Account</h1>
                <p>Offered to established businesses who do not wish to switch their main bank account</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Credit Interest</th>
                                <th>Borrowing/Overdraft</th>
                        </tr>
                </thead>
                <tbody>
	"""
	welcome=welcome+qry_bca_json_msgs('STANDARD')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab4" />
        <label for="tab4">Agricultural</label>
        <div id="tab-content4" class="content">
                <h1>Agricultural Business Account</h1>
                <p>Typically offers rates, fees & charges tailored to the needs of agricultural businesses</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Credit Interest</th>
                                <th>Borrowing/Overdraft</th>
                        </tr>
                </thead>
                <tbody>
	"""
	welcome=welcome+qry_bca_json_msgs('AGRI')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab5" />
        <label for="tab5">Non-commercial</label>
        <div id="tab-content5" class="content">
                <h1>Non-commercial Business Account</h1>
                <p>Offered to non-commercial organisations e.g. schools, charities, credit unions, clubs & societies</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Credit Interest</th>
                                <th>Borrowing/Overdraft</th>
                        </tr>
                </thead>
                <tbody>
	"""
	welcome=welcome+qry_bca_json_msgs('NONCOMM')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"</html>"

	return welcome
