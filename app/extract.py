import json
response="""{"results":[{"update_timestamp":"2018-01-25T20:49:51.336816Z","account_id":"2436403d1dc3e054f7e0795da824a332","account_type":"TRANSACTION","display_name":"FlexDirect Account","currency":"GBP","account_number":{"iban":"GB54NAIA07024646201666","swift_bic":"NAIAGB21","number":"46201666","sort_code":"070246"},"provider":{"display_name":"Nationwide","provider_id":"nationwide","logo_uri":"https://auth.truelayer.com/img/banks/banks-icons/nationwide-icon.svg"}},{"update_timestamp":"2018-01-25T20:49:51.3368492Z","account_id":"8f8dec0f8cd9f19de5b2e0b055b08050","account_type":"SAVINGS","display_name":"e-Savings","currency":"GBP","account_number":{"iban":"GB44NAIA07004050731748","swift_bic":"NAIAGB21","number":"50731748","sort_code":"070040"},"provider":{"display_name":"Nationwide","provider_id":"nationwide","logo_uri":"https://auth.truelayer.com/img/banks/banks-icons/nationwide-icon.svg"}},{"update_timestamp":"2018-01-25T20:49:51.3368594Z","account_id":"888b2776abda70824621ac7f659268af","account_type":"SAVINGS","display_name":"e-ISA","currency":"GBP","account_number":{"iban":"GB97NAIA07009333333334","swift_bic":"NAIAGB21","number":"33333334","sort_code":"070093"},"provider":{"display_name":"Nationwide","provider_id":"nationwide","logo_uri":"https://auth.truelayer.com/img/banks/banks-icons/nationwide-icon.svg"}}],"status":"Succeeded"}"""
resp_dict=json.loads(response)
html="""
<html><table><thead><th>Account ID</th><th>Account Type</th><th>Account Name</th><th>Currency</th><th>IBAN</th><th>SWIFT BIC</th><th>Account Number</th><th>Sort Code</th>
<tbody>"""
for results in resp_dict['results']:
	html=html+"<tr>"
	html=html+"<td>"+results['account_id']+"</td>"
	html=html+"<td>"+results['account_type']+"</td>"
	html=html+"<td>"+results['display_name']+"</td>"
	html=html+"<td>"+results['currency']+"</td>"
	html=html+"<td>"+results['account_number']['iban']+"</td>"
	html=html+"<td>"+results['account_number']['swift_bic']+"</td>"
	html=html+"<td>"+results['account_number']['number']+"</td>"
	html=html+"<td>"+results['account_number']['sort_code']+"</td>"
	html=html+"</tr>"
html=html+"</tbody></table></html>"
print(html)
