#!/usr/bin/python
def qry_pca_json_msgs( filter ) : 
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
	if filter=='Young Person':
		filter_str = "'[\"Youth\"]','[\"YoungAdult\"]'"
	else:
		filter_str = "'[\"" + filter + "\"]'"
	qry_string="""
	select distinct Brand, ProductSegment, ProductName, ProductURL, 
CreditInterest, overdraft, case when overdraft is not null then translate((jsonb_array_elements(overdraft)->'MaximumMonthlyOverdraftCharge')::text,'\"','')::float end as MMC 
from pca_json_view
where productsegment::text in (
""" + filter_str + ") order by case when overdraft is not null then  translate((jsonb_array_elements(overdraft)->'MaximumMonthlyOverdraftCharge')::text,'\"','')::float end "

	cur.execute (qry_string)

	pca_json_res=''

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

		for brand, productsegment, product, producturl, interest, overdraft, mmc in cur.fetchall():
 
			pca_json_res=pca_json_res+"\n<div class=\"row\">"
                        
            #Fetch brand & product information
			pca_json_res=pca_json_res+"\n<td class=\"col-xs-4\"><img src='"
			pca_json_res=pca_json_res+logos[brand]+"'><br>"
			pca_json_res=pca_json_res+"<a href=\""+producturl[0]+"\" target=\"_blank\">"+str(product)+"</a></td>"

			#Fetch credit interest information
			if interest['CreditCharged']==0:
				interest='No interest is paid on this account'
			elif 'CreditInterestGroup' in interest:
				for intgrp in interest['CreditInterestGroup']:
					try:
						interest="Notes:"+intgrp['CreditInterestItem']['InterestNotes']+"<br>"
					except:
						interest="Notes: Not supplied"
						
			if filter in ['Young Person']:
				pca_json_res=pca_json_res+"<td class=\"col-xs-4\">"+str(interest)+"</td>"
			elif filter not in ['Basic']:
				pca_json_res=pca_json_res+"<td class=\"col-xs-4\">"+str(interest)+"</td>"
			else: 
				pca_json_res=pca_json_res+"<td class=\"col-xs-4\"></td>"

			pca_json_res=pca_json_res+"</div>"

			#Fetch overdraft information
			if filter in ('Student','Graduate','General','Packaged','Reward','Premium'):
				pca_json_res=pca_json_res+"<td class=\"col-xs-4\">"	
				if overdraft:    
					for ovd in overdraft:
						if 'MaximumMonthlyOverdraftCharge' in ovd:
								pca_json_res=pca_json_res+"Maximum Monthly Charge (MMC): £"+str(mmc)+"<br>"
						if 'OverdraftPricing' in ovd:
							ovdpricing=ovd['OverdraftPricing']
							if 'Tiers' in ovdpricing:
								for tiers in ovdpricing['Tiers']:
									if 'TierType' in tiers:
										for tiertype in tiers['TierType']:
											pca_json_res=pca_json_res+"Tier Type:"+ tiertype + "<br>"
									if 'TierValueMinimum' in tiers:
										pca_json_res=pca_json_res+"£"+tiers['TierValueMinimum']+" to "
									else:
										pca_json_res=pca_json_res+"Unbounded to "
									if 'TierValueMaximum' in tiers:
										pca_json_res=pca_json_res+"£"+tiers['TierValueMaximum']+"<br>"
									else:
										pca_json_res=pca_json_res+"unbounded<br>"
							if 'InterestRateEARpa' in ovd['OverdraftPricing']:
								pca_json_res=pca_json_res+"EAR:"+ovd['OverdraftPricing']['InterestRateEARpa']+"%<br>"
				pca_json_res=pca_json_res+"</td>"



	except: traceback.print_exc()

        #Close the connection
	myConnection.close()
	
	return pca_json_res
