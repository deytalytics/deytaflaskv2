def atmlocator(postcode, latitude, longitude):
	import psycopg2
	import requests
	import json
	from app.qry_atm_json_msgs import qry_atm_json_msgs
	
	#If we have a postcode but no latitude & longitude
	if not (latitude and longitude) and postcode:
		response = requests.get ("http://api.postcodes.io/postcodes/"+str(postcode), verify=True)
		respstr=json.loads(response.text)
		if respstr['status']!=404:
			latitude=respstr["result"]["latitude"]
			longitude=respstr["result"]["longitude"]
		else:
			welcome="<html><body>Sorry, you need to type in a valid postcode. Hit back button to return</body></html>"
			return welcome
		
	welcome="""
<!DOCTYPE html>
<html lang="en">
<head>
  <title>ATM Locator</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js"></script>
  <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-133427054-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-133427054-1');
</script>
  <style>
       #map {
	   height: 80vh;
       }
  </style>
</head>

  <body>
    <div>
	<h3> 
			<a href="/"><img style="vertical-align:middle" src="images/deytalytics-icon.png" width="50px"></a>
			<span style="">ATM Locator</span>
	</h3>
	</div>
	<div id="helptext">
	Click on an icon to reveal the ATM details
	</div>
	<form action="atmlocator">
	<img src="images/currloc.png" width="30" height="30" onclick="getLocation();"/>"""
	welcome=welcome+"""
	Postcode:<input type="text" id="postcode" maxlength="8" size="8" name="postcode" value=\""""+str(postcode)+"""\">
    <input type="hidden" id="latitude" name="latitude" size="8" value="">	
	<input type="hidden" id="longitude" name="longitude" size="8" value="">	
    """

	#Default the ATM locator to 1 mile - suitable for london
	range=1
	zoom=13

	welcome=welcome+"""
	</form>
    <div id="map"></div>
    <script>
"""		
	zoom, result=qry_atm_json_msgs(latitude, longitude, range, zoom)
	welcome=welcome+"""
		function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: """+str(zoom)+""",
          center: {lat: """+str(latitude)+""", lng: """+str(longitude)+"""}
        });
		
		"""
	welcome=welcome+str(result)
	welcome=welcome+"""
      }
    </script>
	<script>
  var latitude=document.getElementById("latitude");
  var longitude=document.getElementById("longitude");
  
  
  function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    latitude.value = position.coords.latitude
	longitude.value = position.coords.longitude
	postcode.value=''
	window.location.href = "/atmlocator?latitude="+latitude.value+"&longitude="+longitude.value;
	this.form.submit;
}
</script>
    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC5ixy2U-2dgIyY5kSMtLmsE2hYN0bidjE&callback=initMap">
    </script>
  </body>
</html>"""
	return welcome