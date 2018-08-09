def mk_pca_html():
	from qry_pca_json_msgs import qry_pca_json_msgs

	welcome = """
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	  <title>Personal Current Account Price Comparison</title>
	  <link  rel="stylesheet" type="text/css" href="static/tabs.css">
	  <link  rel="stylesheet" type="text/css" href="static/scrolltable.css">
	</head>
	<body>
	  <ul class="tabs">
	"""

	welcome=welcome+"""
	    <li class="tab">
	        <input type="radio" name="tabs" id="tab1" />
        	<label for="tab1">Young Person</label>
        	<div id="tab-content1" class="content">
		<h1>Young Person Bank Account</h1>
		<p>Pitched at young people generally aged anywhere between 11 and 19 (age limit varies with provider). They do not provide an overdraft facility and typically provide basic debit and cashcards. They more often pay in-credit interest than equivalent general bank accounts, in order to encourage savings</p> 
  		<table class="fixed_headers">
  		<thead>
    			<tr>
      				<th>Brand</th>
      				<th>Product Information</th>
      				<th>Credit Interest</th>
    			</tr>
  		</thead>
  		<tbody>
	"""
	welcome=welcome+qry_pca_json_msgs('Young Person')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
	    <li class="tab">
	        <input type="radio" name="tabs" id="tab3" />
	        <label for="tab3">Student</label>
	        <div id="tab-content3" class="content">
	    <p style="background-color:white; color:red">Note: Product comparisons are now provided by the UK's 9 leading banks, ordered by the maximum monthly charge that you will pay, should you exceed your agreed credit limit.</p>
		<h1>Student Account</h1>
                <p>Typically offers increased overdraft limits as the account holder progresses through their academic career.</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Borrowing/Overdraft</th>
                                <th>Benefits</th>
                                <th id="canhide">Credit Interest</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('Student')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
	    <li class="tab">
	        <input type="radio" name="tabs" id="tab4" />
	        <label for="tab4">Graduate</label>
	        <div id="tab-content4" class="content">
	    <p style="background-color:white; color:red">Note: Product comparisons are now provided by the UK's 9 leading banks, ordered by the maximum monthly charge that you will pay, should you exceed your agreed credit limit.</p>
		<h1>Graduate Bank Account</h1>
                <p>Reduces overdraft limits progressively after an account holder has graduated in order to ease them out of relying on credit.</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Borrowing/Overdraft</th>
								<th id="canhide">Credit Interest</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('Graduate')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab5" />
        <label for="tab5">Basic</label>
        <div id="tab-content5" class="content">
		<h1>Basic Bank Accounts</h1>
		<p>Offered to account holders who are ineligible for the other accounts. Offers basic services, typically providing a cash card or prepaid debit card, and not allowing overdraft, direct debit or standing order facilities to be established</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Features</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('Basic')
	welcome=welcome+"</tbody></table></div></li>"


	welcome=welcome+"""
    <li class="tab">
        <input type="radio" checked="checked" name="tabs" id="tab6" />
        <label for="tab6">General</label>
        <div id="tab-content6" class="content">
	    <p style="background-color:white; color:red">Note: Product comparisons are now provided by the UK's 9 leading banks, ordered by the maximum monthly charge that you will pay, should you exceed your agreed credit limit.</p>
		<h1>General Bank Accounts</h1>
		<p>Generally free and offer general banking facilities that you would expect such as access to an overdraft, debit card, cheque book, possibly some in-credit interest, direct debit and standing order set up. To get this account type, you cannot have a poor credit history and you may need to deposit a minimum amount per month</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Borrowing/Overdraft</th>
                                <th>Benefits</th>
                                <th id="canhide">Credit Interest</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('General')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab7" />
        <label for="tab7">Packaged</label>
        <div id="tab-content7" class="content">
	    <p style="background-color:white; color:red">Note: Product comparisons are now provided by the UK's 9 leading banks, ordered by the maximum monthly charge that you will pay, should you exceed your agreed credit limit.</p>
		<h1>Packaged Bank Accounts</h1>
		<p>Offers a set of typically pre-defined benefits for a monthly fee</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Borrowing/Overdraft</th>
                                <th>Benefits</th>
                                <th id="canhide">Credit Interest</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('Packaged')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab8" />
        <label for="tab8">Reward</label>
        <div id="tab-content8" class="content">
	    <p style="background-color:white; color:red">Note: Product comparisons are now provided by the UK's 9 leading banks, ordered by the maximum monthly charge that you will pay, should you exceed your agreed credit limit.</p>
		<h1>Reward Bank Accounts</h1>
		<p>Focuses on "Rewards" e.g. cashback or offers from retailers. Typically charges a fee</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Borrowing/Overdraft</th>
								<th>Benefits</th>
                                <th id="canhide">Credit Interest</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('Reward')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"""
    <li class="tab">
        <input type="radio" name="tabs" id="tab9" />
        <label for="tab9">Premium</label>
        <div id="tab-content9" class="content">
		<p style="background-color:white; color:red">Note: Product comparisons are now provided by the UK's 9 leading banks, ordered by the maximum monthly charge that you will pay, should you exceed your agreed credit limit.</p>
		<h1>Premium Bank Accounts</h1>
		<p>Offered to account holders who earn relatively high salaries and commit to depositing a certain amount of money per month. Typically comes with a charge in return for high value benefits</p>
                <table class="fixed_headers">
                <thead>
                        <tr>
                                <th>Brand</th>
                                <th>Product Information</th>
                                <th>Borrowing/Overdraft</th>
								<th>Benefits</th>
                                <th id="canhide">Credit Interest</th>
                        </tr>
                </thead>
                <tbody>
	"""

	welcome=welcome+qry_pca_json_msgs('Premium')
	welcome=welcome+"</tbody></table></div></li>"

	welcome=welcome+"</html>"
	return welcome
