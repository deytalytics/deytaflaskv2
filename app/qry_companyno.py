def qry_companyno(i):
	import requests
	import json
	import sys
	import csv
	from os import curdir
	r={}
	print("companyno="+str(i))

	with open('app/SICCodes.csv', mode='r') as infile:
		reader = csv.reader(infile)
		siccodes = {rows[0]:rows[1] for rows in reader}


	auth=('FzYg4_ufx-_dYc3hZKt51XnnejZFg-V59lSfQJBh','')
	url='https://api.companieshouse.gov.uk/company/'+str(i)
	r=requests.get(url,auth=auth)

	try:
		json_data=json.loads(r.content.decode('utf-8'))
		retstr="Deytalytics Ltd. would very much like to welcome the following newly incorporated companies"
		retstr=retstr+"<br><br><b>Company Number:</b>"+json_data['company_number']
		retstr=retstr+"<br><b>Company Name:</b><a href=\"https://www.google.co.uk/search?q="+json_data['company_name'].replace(' ','+')+"\" target=\"_blank\">"+json_data['company_name']+"</a>"
		retstr=retstr+"<br><b>Incorporation Date:</b>"+json_data['date_of_creation']
		if 'address_line_1' in json_data['registered_office_address']:
			retstr=retstr+"<br><b>Address Line 1:</b>"+str(json_data['registered_office_address']['address_line_1'])
		else:
			retstr=retstr+"<br><b>Address Line 1:</b>"
		if 'address_line_2' in json_data['registered_office_address']:
			retstr=retstr+"<br><b>Address Line 2:</b>"+str(json_data['registered_office_address']['address_line_2'])
		else:
			retstr=retstr+"<br><b>Address Line 2:</b>"
		if 'locality' in json_data['registered_office_address']:
			retstr=retstr+"<br><b>Locality:</b>"+str(json_data['registered_office_address']['locality'])
		else: 
			retstr=retstr+"<br><b>Locality:</b>"
		if 'postal_code' in json_data['registered_office_address']:
			retstr=retstr+"<br><b>Postcode:</b><a href=\"http://google.co.uk/maps?q="+str(json_data['registered_office_address']['postal_code']).replace(' ','+')+"\" target=\"_blank\">"+str(json_data['registered_office_address']['postal_code'])+"</a>" 
		try:
			retstr=retstr+"<br><br><b>SICCode:</b>"+str(siccodes[json_data['sic_codes'][0]])
		except:
			retstr=retstr+"<br><br><b>SICCode:</b> Unknown"+str(json_data['sic_codes'][0])
		
	
		return retstr
	
	except:
		retstr="Skipping record due to special characters"
		url='https://api.companieshouse.gov.uk/company/'+str(i)
		r=requests.get(url,auth=auth)
		return retstr
	
