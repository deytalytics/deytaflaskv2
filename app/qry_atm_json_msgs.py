#!/usr/bin/python
def qry_atm_json_msgs(lat, long, area, zoom) : 
	import sys
	import json
	import psycopg2

	hostname = 'ec2-50-16-196-138.compute-1.amazonaws.com'
	username = 'kbmymanebzaprn'
	password = 'a090dbaf8e346e65ea63436b9d22c6e709f786308c0f4744e4d257389c71a8fa'
	database = 'de3gnfncn93kt4'

	#Connect to the database
	myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

	cur=myConnection.cursor()
	if not area:
		range=0.05
	else:
		range=0.02347*float(area)
	qry_string="""
select brand, latitude, longitude, buildingnumber, streetname, townname, postcode, atmservices, locationcategory
from atm_json_view
where latitude between """+str(lat-range)+""" and """+str(lat+range)+"""
and longitude between """+str(long-range)+""" and """+str(long+range)
	cur.execute (qry_string)

	atm_json_res=''

	halifax="var image={url:'http://www.userlogos.org/files/logos/macleod.mac/halifax.u.png', scaledSize: new google.maps.Size(50, 50)};"
	nationwide="var image={url:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1k24H30PRLEKtWovF41OYeE3Ew6opaLobKtfyE0OU85qr24s9Aw', scaledSize: new google.maps.Size(25, 25)};"
	hsbc="var image={url:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf9Dm6-t1BiMqhh2sLpyhLzwKiRLfNqPKBYnUYZXCzEVDxz8VL', scaledSize: new google.maps.Size(25, 25)};"
	barclays="var image={url:'https://static-s.aa-cdn.net/img/ios/636504159/b699e896b260b52dc7c7cc7c23dec913', scaledSize: new google.maps.Size(25, 25)};"
	lloyds="var image={url:'https://www.lloydsbank.com/assets/img/personal/lloyds_personal_banking_logo_m.png', scaledSize: new google.maps.Size(25, 25)};"
	santander="var image={url:'https://logo.clearbit.com/santander.com', scaledSize: new google.maps.Size(25, 25)};"
	natwest="var image={url:'http://personal.natwest.com/etc/designs/dmp_natwest/favicon.ico', scaledSize: new google.maps.Size(25, 25)};"
	rbs="var image={url:'http://pbs.twimg.com/profile_images/557489898018459648/wnP2DMIe_normal.png', scaledSize: new google.maps.Size(25, 25)};"
	ulsterbank="var image={url:'https://pbs.twimg.com/profile_images/481434724317945859/bspl1Agb_normal.jpeg', scaledSize: new google.maps.Size(25, 25)};"
	bankofscotland="var image={url:'http://carilloncapital.com/newsitecarillon/wp-content/uploads/2014/06/imgres-3.jpg', scaledSize: new google.maps.Size(25, 25)};"
	bankofireland="var image={url:'https://pbs.twimg.com/profile_images/618717342986575876/T3XrKqYV_400x400.jpg', scaledSize: new google.maps.Size(25,25)};"
	danskebank="var image={url:'https://pbs.twimg.com/profile_images/840180636220563456/YMP5Jj9d.jpg', scaledSize: new google.maps.Size(25,25)};"
	firsttrustbank="var image={url:'https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/First_Trust_Bank_logo.svg/100px-First_Trust_Bank_logo.svg.png', scaledSize: new google.maps.Size(25,25)};"
	rest="var image={url:'https://cdn4.iconfinder.com/data/icons/BRILLIANT/accounting/png/32/atm.png'};"
	i=1
	for brand, latitude, longitude, buildingnumber, streetname, townname, postcode, atmservices, locationcategory in cur.fetchall():
		if brand=="Halifax":
			atm_json_res=atm_json_res+halifax
		elif brand=="Nationwide":
			atm_json_res=atm_json_res+nationwide
		elif brand=="HSBC Group":	
			atm_json_res=atm_json_res+hsbc
		elif brand=="Barclays Bank":	
			atm_json_res=atm_json_res+barclays
		elif brand=="Lloyds Bank":	
			atm_json_res=atm_json_res+lloyds
		elif brand=="Santander UK":	
			atm_json_res=atm_json_res+santander
		elif brand=="NatWest":
			atm_json_res=atm_json_res+natwest
		elif brand=="Royal Bank of Scotland":
			atm_json_res=atm_json_res+rbs
		elif brand=="Ulster Bank":
			atm_json_res=atm_json_res+ulsterbank
		elif brand=="Bank of Scotland":
			atm_json_res=atm_json_res+bankofscotland
		elif brand=="Bank of Ireland":
			atm_json_res=atm_json_res+bankofireland
		elif brand=="Dankse Bank":
			atm_json_res=atm_json_res+danskebank
		elif brand=="First Trust Bank":
			atm_json_res=atm_json_res+firsttrustbank
		else:
			atm_json_res=atm_json_res+rest
		atm_json_res=atm_json_res+"var label='<b>"+brand+"</b><br>"
		if buildingnumber:
			atm_json_res=atm_json_res+buildingnumber+"<br>"
		if streetname:
			atm_json_res=atm_json_res+streetname.replace("'","\'")+"<br>"
		if townname:
			atm_json_res=atm_json_res+townname+"<br>"
		if postcode:
			atm_json_res=atm_json_res+postcode+"<br>"
		if atmservices:
			atm_json_res=atm_json_res+"<b>ATMServices:</b>"+str(atmservices)[1:-1].replace("'", "")+"<br>"
		if locationcategory:
			atm_json_res=atm_json_res+"<b>LocationCategory:</b>"+str(locationcategory[1:-1])+"<br>"
		atm_json_res=atm_json_res+"<a href=\"https://maps.google.com/maps?q="+str(latitude)+","+str(longitude)+"&z=16\">View on Google Maps</a> for directions"
		atm_json_res=atm_json_res+"';"
		atm_json_res=atm_json_res+"var infowindow"+str(i)+" = new google.maps.InfoWindow({content: label});"
		atm_json_res=atm_json_res+"var marker"+str(i)+" = new google.maps.Marker({position: {lat: "+str(latitude)+", lng: "+str(longitude)+"}, map: map, icon: image});"
		atm_json_res=atm_json_res+"google.maps.event.addListener(marker"+str(i)+", 'click', function() {infowindow"+str(i)+".open(map,marker"+str(i)+");});"
		i+=1
	myConnection.close()

	#Add a marker for the actual location user chose
	atm_json_res=atm_json_res+"var image={url:'http://pbs.twimg.com/profile_images/557489898018459648/wnP2DMIe_normal.png', scaledSize: new google.maps.Size(25, 25)};"
	atm_json_res=atm_json_res+"var marker = new google.maps.Marker({position: {lat: "+str(lat)+", lng: "+str(long)+"}, map: map});"

	#If there are less than 10 ATMs returned then lets widen the search area
	if i<=5:
		area=area*5
		zoom-=1
		zoom, atm_json_res=qry_atm_json_msgs(lat,long,area,zoom)
		
	print(atm_json_res)


	return zoom, atm_json_res