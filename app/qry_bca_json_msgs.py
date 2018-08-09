#!/usr/bin/python
def qry_bca_json_msgs( filter ) : 
	import sys
	import json
	import psycopg2
	import traceback

	hostname = 'aa1q1kus00tfvcf.cicyn2v77if2.us-west-2.rds.amazonaws.com'
	username = 'nesta'
	password = 'xedos123'
	database = 'nesta'

	#Connect to the database
	myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
	cur=myConnection.cursor()

	print(filter)

	if filter=='NONCOMM':
		qry_string="select brand, ProductSegment, ProductName, ProductURL, CreditInterest, Overdraft from bca_json_view where productname::text like '%Chari%' or productname::text like '%Club%' or productname::text like '%Union%' or productname::text like '%School%'"
	elif filter=='ESTABLISHED':
		qry_string="select brand, ProductSegment, ProductName, ProductURL, CreditInterest, Overdraft from bca_json_view where upper(translate(productname::text,'-','')) not like '%STARTUP%' and Overdraft is not null"
	else:
		qry_string="select brand, ProductSegment, ProductName, ProductURL, CreditInterest, Overdraft from bca_json_view where upper(translate(productname::text,'-','')) like '%" + filter + "%'"

	cur.execute (qry_string)

	bca_json_res=''

	try:
		logos={"Lloyds Bank": "https://pbs.twimg.com/profile_images/887961982741204992/WdcJMiTi.jpg",
		   "Bank of Ireland": "https://pbs.twimg.com/profile_images/618717342986575876/T3XrKqYV_400x400.jpg",
		   "Barclays Bank":"https://pbs.twimg.com/profile_images/378800000294050709/731497a6b61ffe8b6e8e44f78b51b442_400x400.png",
		   "Bank of Scotland": "http://www.lloydsbankinggroup.com/globalassets/images/logos/645-x/bos-645x339.png",
		   "HSBC Group":"https://pbs.twimg.com/profile_images/880372947998961664/f7hq8f5u_400x400.jpg",
		   "Nationwide":"https://pbs.twimg.com/profile_images/770597713893285888/ItnmL0YM.jpg",
		   "Danske Bank":"https://pbs.twimg.com/profile_images/840180636220563456/YMP5Jj9d.jpg",
		   "Royal Bank of Scotland":"https://pbs.twimg.com/profile_images/755776046054637568/sKs1AMKR.jpg",
		   "NatWest":"https://pbs.twimg.com/profile_images/930091054665256961/VMiXki2j.jpg",
		   "Santander UK":"https://pbs.twimg.com/profile_images/509756032768147457/72_qkXZ-.png",
		   "First Trust Bank":"https://pbs.twimg.com/profile_images/648796406153670656/ivu8xbCA.jpg",
		   "Adam & Company":"http://bwsltd.co.uk/wp-content/uploads/2015/05/Adamco-logo-300x218.gif",
		   "Allied Irish Bank (GB)":"https://pbs.twimg.com/profile_images/890884394680020992/RolNyU9a_400x400.jpg",
		   "Ulster Bank":"https://pbs.twimg.com/profile_images/481434724317945859/bspl1Agb_400x400.jpeg",
		   "Coutts":"https://pbs.twimg.com/profile_images/2238163472/coutts_twitter_400x400.png"}

		for brand, productsegment, product, producturl, interest, overdraft in cur.fetchall():
			bca_json_res=bca_json_res+"\n<tr>"

			#Fetch brand & product url
			bca_json_res=bca_json_res+"\n<td class=\"col-xs-4\"><img src='"
			bca_json_res=bca_json_res+logos[brand]+"'><br>"
			bca_json_res=bca_json_res+"<a href=\""+producturl[0]+"\" target=\"_blank\">"+str(product)+"</a></td>"

			#Fetch credit interest rates
			if interest['CreditCharged']==0:
				interest='No interest is paid on this account'
			else:
				interest='Interest is available on this account. See site for details'
			bca_json_res=bca_json_res+"\n<td class=\"col-xs-4\">"+interest+"</td>"

			#Fetch overdraft rates
			bca_json_res=bca_json_res+"\n<td class=\"col-xs-4\">"	
			if overdraft:
				for ovd in overdraft:
					if 'OverdraftPricing' in ovd:
						ovdpricing = ovd['OverdraftPricing']
						if 'Tiers' in ovdpricing:
							for tiers in ovdpricing['Tiers']:
								if 'TierType' in tiers:
									for tiertype in tiers['TierType']:
										bca_json_res=bca_json_res+"Tier Type:"+ tiertype + "<br>"
								if 'TierValueMinimum' in tiers:
									bca_json_res=bca_json_res+"£"+tiers['TierValueMinimum']+" to "
								else:
									bca_json_res=bca_json_res+"Unbounded to "
								if 'TierValueMaximum' in tiers:
									bca_json_res=bca_json_res+"£"+tiers['TierValueMaximum']+"<br>"
								else:
									bca_json_res=bca_json_res+"unbounded<br>"
						if 'InterestRateEARpa' in ovdpricing:
							bca_json_res=bca_json_res+"EAR: "+ovd['OverdraftPricing']['InterestRateEARpa']+"%<br><br>"
						else:
							bca_json_res=bca_json_res + "No overdraft rate (EAR) has been supplied.<br><br>"
				bca_json_res=bca_json_res+"<br>"
			else:
				bca_json_res=bca_json_res + "No overdraft is available for this account<br><br><br><br><br><br>"
				
			bca_json_res=bca_json_res+"</td>\n</tr>"

	except: traceback.print_exc()
		
	#Close the connection
	myConnection.close()
	return bca_json_res
