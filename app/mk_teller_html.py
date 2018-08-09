def mk_teller_html():
	import requests
	app_id="19db7f7c-2d2e-48a8-9b1d-01c728e717ee"
	permissions="full_account_number:true, balance:true, transaction_history:true, external_payments:true"
	resp=requests.get("https://auth.truelayer.com/?response_type=code&client_id=deypay-dvbg&nonce=4247001561&scope=info%20accounts%20balance%20transactions%20cards%20offline_access&redirect_uri=https://console.truelayer.com/redirect-page&enable_mock=true")
	welcome=resp.text
	return welcome
