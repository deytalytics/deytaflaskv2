def companies():
	import psycopg2
	import requests
	import json

	hostname = 'aa1q1kus00tfvcf.cicyn2v77if2.us-west-2.rds.amazonaws.com'
	username = 'nesta'
	password = 'xedos123'
	database = 'nesta'

	#Connect to the database
	myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
	cur=myConnection.cursor()
		
	welcome="""
<!DOCTYPE html>
<html>
  <head>
    <style>
       #map {
	   height: 80vh;
       }
    </style>
	
  </head>
  <body>
  <script>
function replace_helptext(ctr) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById(\"helptext\").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "qry_companyno?s="+ctr, true);
  xhttp.send();
}
</script>

  <script>
  var s=1;
  var x=setInterval(function() {
    replace_helptext(s+=1);
}, 1000);
   </script>
   
    <div>
	<h3> 
			<img style="vertical-align:middle" src="static/deytalyticslogo.png">
			<span style="">UK Newly Incorporated Companies</span>
	</h3>
	</div>
	<div id="helptext">
	</div>
	<img background="static/incorporation.jpg">
  </body>
</html>"""
	return welcome