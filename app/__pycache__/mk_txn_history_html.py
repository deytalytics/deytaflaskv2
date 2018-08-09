def mk_txn_history_html():

	welcome = """
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<title>Bank of Deytalytics Transaction History</title>
	<link rel="shortcut icon" type="image/png" href="/media/images/favicon.png">
	<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="http://www.datatables.net/rss.xml">
	<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css">
	<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
	<style type="text/css" class="init">
	
	</style>
	<script type="text/javascript" language="javascript" src="//code.jquery.com/jquery-1.12.4.js">
	</script>
	<script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js">
	</script>
	<script type="text/javascript" class="init">
	

$(document).ready(function() {
	$('#example').DataTable();
} );
	</script>
	
</head>
<body class="wide comments example">
	<script>
		function myPromo(){
			alert($(this).attr("class"));
    };
	</script>
	<a name="top" id="top"></a>
	<div class="container">
		<div class="fw-body">
			<div class="content">
				<h1>Bank of <img src="static/deytalyticslogo.png"></h1>
				<h3 class="page_title">Transaction History</h3>
				<table id="example" class="display" cellspacing="0" width="100%">
					<thead>
						<tr>
							<th>Date</th>						
							<th>Bank</th>
							<th>Account</th>
							<th>Category</th>
							<th>Payee</th>
							<th>Amount</th>
							<th>Balance</th>
						</tr>
					</thead>
					<tbody>
  <tr>
  <td class=xl67>2017-12-03-15.17</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td><a href="https://www.yelp.co.uk/search?find_desc=zagat%2Brated%2Brestaurants&find_loc=London" target="_blank">Eating Out</td>
  <td><a href="https://www.hartsboatyard.co.uk/content/pcdg/south-east/hartsboatyard/tablebooking" target="_blank">Harts Boatyard Surbiton</td>
  <td align=right>-88.25</td>
  <td align=right>487.02</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-03-09.46</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Entertainment</td>
  <td><a href="http://hamptoncourtpalaceicerink.co.uk/" target="_blank">Hampton Court Ice Rink</td>
  <td align=right>-17.00</td>
  <td align=right>504.02</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-02-20.03</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td><a href="https://www.yelp.co.uk/search?find_desc=zagat%2Brated%2Brestaurants&find_loc=London" target="_blank">Eating Out</td>
  <td><a href="http://www.lanonna.co.uk/contact.html" target="_blank">La Nonna Wimbledon</td>
  <td align=right>-86.72</td>
  <td align=right>590.74</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-02-17.35</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Shopping</td>
  <td><a href="https://www.whsmith.co.uk/" target="_blank">WH Smith Trident<span style='mso-spacerun:yes'> </span></td>
  <td align=right>-4.99</td>
  <td align=right>595.73</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-02-17.15</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Shopping</td>
  <td><a href="http://www.argos.co.uk/stores/507-colliers-wood-argos-and-ee-store" target="_blank">Argos Colliers Wood</td>
  <td align=right>-39.99</td>
  <td align=right>635.72</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-02-12.17</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Entertainment</td>
  <td><a href="http://mobi.odeon.co.uk/cinemas/wimbledon/142/" target="_blank">Odeon Wimbledon</td>
  <td align=right>-24.50</td>
  <td align=right>660.22</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-01-16.59</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td><a href="https://www.yelp.co.uk/search?find_desc=zagat%2Brated%2Brestaurants&find_loc=London" target="_blank">Eating Out</td>
  <td><a href="http://www.burgerking.co.uk/offers" target="_blank">Burger King</td>
  <td align=right>-10.99</td>
  <td align=right>671.21</td>
 </tr>
 <tr>
  <td class=xl67>2017-12-01-13.21</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Shopping</td>
  <td><a href="https://www.sainsburys.co.uk/webapp/wcs/stores/servlet/gb/groceries/great-offers?langId=44&storeId=10151&krypto=EWiRkogD0N16dSC5Onj9LppgxIi2YSbDuEQ01YdQbwP7nOJ6uZIhn6lCOebTNle6LpuSZorH0mscqgeV%2BqjiCTaf%2FyR5%2FJM4JexNUj2lbR7qYQQS9cQ5OrUzD%2BEAuMVfPtFeFOI0d2VIHtADbildqGwpSFkNRG2d0cuf46JpAT4%3D&ddkey=https%3Agb%2Fgroceries%2Fgreat-offers" target="_blank">Sainsburys Merton</td>
  <td align=right>-34.12</td>
  <td align=right>705.33</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-30-00.00</td>
  <td>HSBC</td>
  <td><a href="https://advancemembers.hsbc.co.uk/login" target="_blank">Advance</td>
  <td class="bills">Bills</td>
  <td><a href="https://my.virginmedia.com/home/index" target="_blank">Virgin Media</td>
  <td align=right>-42.13</td>
  <td align=right>747.46</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-29-17.59</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Shopping</td>
  <td><a href="https://stores.wilko.com/gb/london/19-21-mitcham-road" target="_blank">Wilko Tooting</td>
  <td align=right>-3.72</td>
  <td align=right>751.18</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-28-13.23</td>
  <td>HSBC</td>
  <td><a href="https://advancemembers.hsbc.co.uk/login" target="_blank">Advance</td>
  <td>Bills</td>
  <td><a href="https://sse.co.uk/home" target="_blank">SE Gas</td>
  <td align=right>-260.89</td>
  <td align=right>1012.07</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-28-13.10</td>
  <td>HSBC</td>
  <td><a href="https://advancemembers.hsbc.co.uk/login" target="_blank">Advance</td>
  <td>Bills</td>
  <td><a href="https://sse.co.uk/home" target="_blank">Southern Electric</td>
  <td align=right>-160.34</td>
  <td align=right>1172.41</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-27-18.48</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td><a href="https://www.yelp.co.uk/search?find_desc=zagat%2Brated%2Brestaurants&find_loc=London" target="_blank">Eating Out</td>
  <td><a href="https://www.gbk.co.uk/location/wimbledon" target="_blank">GBK Ltd.</td>
  <td align=right>-15.45</td>
  <td align=right>1187.86</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-26-10.21</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td>Entertainment</td>
  <td><a href="http://www.atgtickets.com/venues/new-wimbledon-theatre/" target="_blank">New Wimbledon Theatre</td>
  <td align=right>-62.50</td>
  <td align=right>1250.36</td>
 </tr>
 <tr>
  <td class=xl67>2017-11-24-15.20</td>
  <td>Nationwide</td>
  <td><a href="https://onlinebanking.nationwide.co.uk/AccessManagement/Login" target="_blank">FlexAccount</td>
  <td><a href="https://www.yelp.co.uk/search?find_desc=zagat%2Brated%2Brestaurants&find_loc=London" target="_blank">Eating Out</td>
  <td><a href="https://www.dogandfoxwimbledon.co.uk/" target="_blank">Dog &amp; Fox Wim Village</td>
  <td align=right>-37.20</td>
  <td align=right>1312.86</td>
 </tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
	</div>
<div class="promo"></div>
		
</body>
</html>
"""

	return welcome
