from app import app, username, db
from app.models import Deypay_user, Tokens
from app.forms import LoginForm, RegisterForm
import requests, json, os
from requests_oauthlib import OAuth2Session
from flask import render_template, flash, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

# Replace the client_id, client_secret and redirect_uri info below with the values for these that you entered/obtained upon registration of your application with Truelayer  
# at:- https://console.truelayer.com/settings/application 
heroku_client_id = "deypay-dvbg"
heroku_client_secret = os.environ['HEROKU_CLIENT_SECRET']
heroku_redirect_uri="https://www.deytalytics.com/truelayer/callback"
heroku_nonce= os.environ['HEROKU_NONCE']
gcp_client_id="deypay-9f90ef"
gcp_client_secret=os.environ['GCP_CLIENT_SECRET']
gcp_redirect_uri = "https://deytalytics.co.uk/truelayer/callback"
gcp_nonce=os.environ['GCP_NONCE']
dev_redirect_uri="http://localhost:5000/truelayer/callback"
client_id=gcp_client_id
client_secret=gcp_client_secret
nonce=gcp_nonce
redirect_uri=gcp_redirect_uri
scopes = "info%20accounts%20balance%20transactions%20cards%20offline_access"
authorization_base_url = "https://auth.truelayer.com/?response_type=code&client_id="+client_id+"&nonce="+nonce+"&scope="+scopes+"&redirect_uri="+redirect_uri+"&enable_mock=true"
token_url = "https://auth.truelayer.com/connect/token"
get_acct_url="https://api.truelayer.com/data/v1/accounts"

@app.route('/')
def index():
	from app.mk_homepage_html import mk_homepage_html
	welcome=mk_homepage_html()
	return welcome

@app.route('/getheaders', methods={'GET','POST','OPTIONS'})
def getheaders():
	html="""
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
    $("button").click(function(){
        $.ajax({
		url:'http://www.expedia.com/flight/search/',
		dataType:'JSON',
	    headers: {'Access-Control-Allow-Origin':'*'},	data:{"trips":[{"departureAirportCode":"LGW","arrivalAirportCode":"AYT","departureDate":"2018-10-20","returnDate":null}],"numberOfAdults":2,"childAges":["8"],"infantInLap":[false],"isRefundableFlight":false,"isNonStopFlight":true,"airlinePreference":"","cabinClass":"coach","pageSelectionParameters":{},"packageType":"f","routeType":"OneWay","hashCodeToCheckValidation":"d208f2360455f903fcc4486466c0530b","stubFile":null},function(result){
            $.each(result, function(i, field){
                $("div").append(field + " ");
            });
        },'json');
    });
});
</script>
</head>
<body>

<button>Get JSON data</button>

<div></div>

</body>
</html>

"""
	return html

@app.route('/development_projects')
def dev_projs():
	print('dev_projects')	
	return render_template('dev_projs.html')

@app.route('/alexa_skills')
def alexa():
	from app.mk_alexa_skills_html import mk_alexa_skills_html
	welcome=mk_alexa_skills_html()
	return welcome
	
@app.route('/atmlocator')
def atm():
	from app.atmlocator import atmlocator
	if request.args:
		params=request.args
		if 'postcode' in params and params['postcode']!='':
			postcode=params["postcode"]
		else:	
			postcode=''
		if 'latitude' in params and params['latitude']!='':
			latitude=float(params["latitude"])
		else: 
			latitude=''
		if 'longitude' in params and params['longitude']!='':
			longitude=float(params["longitude"])
		else:
			longitude=''
		welcome=atmlocator(postcode,latitude,longitude)
	else:
		if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
			ip_addr=request.environ['REMOTE_ADDR']
		else:
			ip_addr=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy]
		if "," in ip_addr:
			forwarded_ip = ip_addr.split(",")
			ip_addr=forwarded_ip[0]
		print(ip_addr)
		latitude=51
		longitude=-0.18
		if ip_addr!='127.0.0.1':
			response=requests.get("https://ipinfo.io/"+ip_addr+"/geo")
			print(response.text)
			json_resp=json.loads(response.text)
			geolocation=json_resp['loc'].split(",")
			latitude=float(geolocation[0])
			longitude=float(geolocation[1])
			print("latitude:"+str(latitude)+" longitude:"+str(longitude))
		welcome=atmlocator('',latitude,longitude)  
	return welcome
	
@app.route('/geolocator')
def geolocator():
	return render_template('geolocator.html')

@app.route('/companies_house_reporting')
def companies_house():
	from app.mk_companyhouse_reporting_html import mk_companyhouse_reporting_html
	welcome=mk_companyhouse_reporting_html()	
	return welcome
	
@app.route('/qry_companyno')
def qry_companyno():
	from app.qry_companyno import qry_companyno
	companyno=int(request.args.get('s'))+11679062
	welcome=qry_companyno(companyno)
	return welcome
	
@app.route("/deypay")
def deypay():
	if 'username' in session:
		connected_banks=[]
		if Tokens.query.filter_by(username=session['username']).first():
			for tokens in Tokens.query.filter_by(username=session['username']).all():
				connected_banks.append(tokens.bank)
		return render_template('deypay.html',connected_banks=connected_banks)
	else:
		return redirect(url_for('login'))

@app.route('/deypay/logout')
def logout():
	#Clear out all of the session variables
	session.clear()
    #Display the logout page	
	return render_template('logout.html')

		
@app.route('/deypay/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('deypay'))
	return render_template('login.html',form=form)
@app.route('/deypay/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = Deypay_user(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		session['username']=form.username.data

		return redirect(url_for('deypay'))

	return render_template('signup.html', form=form)

@app.route('/deypay/graphs', methods=['GET'])
def graphs():
	return render_template('graphs.html')

@app.route('/deypay/balance_history_graphs', methods=['GET'])
def balance_history_graphs():
	data=get_transaction_results()
	print (data)
	#List balance history graphs only for those accounts that have a transaction history
	accts = []
	for item in data:
		if (item['transactions']):
			accts.append(item)
	#print(accts)
	return render_template('balance_history_graphs.html',data=accts)	
	
@app.route('/deypay/balance_history', methods=['GET'])
def balance_history():
	if request.args:
		params=request.args
	#Fetch balance
	data=get_balance_results()
	for results in data:
		if (results['account']['display_name']==params['acct']):
			current_balance=results['balance']['current']
	#print("current balance="+str(current_balance))
	#Fetch transactions
	data=get_transaction_results()
	txnhist=[]
	for results in data:
		if (results['account']['display_name']==params['acct']):
			for transactions in results['transactions']:
				date,time=str(transactions['timestamp']).split('T')
				txn_date=date+"T00:00:00"
				txnhist.append({"date":txn_date, "close":transactions['amount']})
	sorted_txnhist=sorted(txnhist, key=lambda k:k["date"], reverse=True)
	balances=[]
	last_txn_date=""
	for running_total in sorted_txnhist:
		txn_date=running_total['date']
		if txn_date != last_txn_date:
			balances.append({"date":txn_date, "close":current_balance})
			last_txn_date=txn_date
		current_balance=current_balance-running_total['close']

	#print(balances)
	return render_template('balance_history.html',data=balances)
	
@app.route("/truelayer")
def truelayer():

	"""Step 1: User Authorization.

	Redirect the user/resource owner to the TrueLayer's Authorisation Server 
	using an URL with a few key OAuth parameters.
	"""

	truelayer = OAuth2Session(client_id)
	authorization_url, state = truelayer.authorization_url(authorization_base_url)

	# State is used to prevent CSRF, keep this for later.
	session['oauth_state'] = state
	session['return']='.deypay'
	authorization_url = authorization_base_url
	return redirect(authorization_url)

@app.route("/truelayer/hangup")
def hangup():
	#If the user has any tokens
	if Tokens.query.filter_by(username=session['username']).first():
		#Remove all of them
		for tokens in Tokens.query.filter_by(username=session['username']).all():
			db.session.delete(tokens)
		db.session.commit()
	return redirect(url_for('.deypay'))

# Step 2: User authorization, this happens on the provider.

@app.route("/truelayer/callback", methods=["GET"])
def callback():
	""" Step 3: Retrieving an access token.

	The user has been redirected back from the provider to your registered
	callback URL. With this redirection comes an authorization code included
	in the redirect URL. We will use that to obtain an access token.
	"""  
	auth_code=request.args.get('code')

	response=requests.post('https://auth.truelayer.com/connect/token', data = {"grant_type":"authorization_code", "code":auth_code, "client_id":client_id, "client_secret": client_secret, "redirect_uri":redirect_uri})
	#print('response.text='+response.text)
	resp_dict=json.loads(response.text)
	access_token=resp_dict['access_token']
	refresh_token=resp_dict['refresh_token']
	# At this point you've got an access token which you can use to access TrueLayer's Account Information API via their Resource Server and a refresh token that can be used to fetch a new access token when it expires. 	
	# Let's fetch and store which bank we connected to
	resp_dict=json.loads(process_response(get_acct_url, access_token, refresh_token))
	connected_bank=resp_dict['results'][0]['provider']['display_name']
	#print('connected_bank='+connected_bank)
	add_tokens(connected_bank, access_token, refresh_token)
	if 'return' in session:
	   return redirect(url_for(session['return']))
	else:
	   return redirect(url_for('.deypay'))

def add_tokens(connected_bank, access_token, refresh_token):
	#print('access_token='+access_token)
	#print('refresh_token='+refresh_token)
	for x in session:
		print("session["+x+"]="+str(session[x]))
	if username in session:
		user=session['username']
	else:
		user=Deypay_user.query.filter_by(id=session['user_id']).first()
	print(user.username)
	new_tokens = Tokens.query.filter_by(username=user.username, bank=connected_bank).first()
	#Either update the user's access tokens if he's already connected to this bank
	if new_tokens:
		new_tokens.access_token=access_token
		new_tokens.refresh_token=refresh_token
	#Or add new tokens for this user for this bank
	else:
		new_tokens = Tokens(username=user.username,bank=connected_bank, access_token=access_token,refresh_token=refresh_token)
		db.session.add(new_tokens)
	#Save changes to database
	db.session.commit()
	return True
	

def refresh_access_token(refresh_token):
	#Call this function when current access token has expired
	#print('refresh_token='+refresh_token)
	response=requests.post('https://auth.truelayer.com/connect/token', data = {"grant_type":"refresh_token", "client_id":client_id, "client_secret": client_secret, "refresh_token": refresh_token})
	print('response.status_code='+str(response.status_code)+' reponse.text='+response.text)
	resp_dict=json.loads(response.text)
	access_token=resp_dict['access_token']
	refresh_token=resp_dict['refresh_token']
	#Retrieve the bank that this access_token is for
	headers = {"Authorization": 'Bearer '+access_token}
	response=requests.get(get_acct_url,  headers=headers)
	resp_dict=json.loads(response.text)
	print('response.text='+response.text)
	connected_bank=resp_dict['results'][0]['provider']['display_name']
	print('connected_bank='+connected_bank)
	#Add tokens to database
	add_tokens(connected_bank, access_token, refresh_token)
	return access_token 
	
def process_response(url,access_token,refresh_token):
	headers = {"Authorization": 'Bearer '+access_token}
	response=requests.get(url,  headers=headers)
	#If we receive back an unauthorised status code as a response, the current access token has expired so we will need to refresh it
	print('response.status_code='+str(response.status_code))
	response_text=response.text
	if response.status_code==401 or response.status_code==403:
	   access_token = refresh_access_token(refresh_token)
	   response_text=process_response(url,access_token,refresh_token)
	return response_text
	
@app.route("/truelayer/acctinfo", methods=["GET"])
def get_acctinfo():
	"""Fetching a protected resource using an OAuth 2 token.
	"""
	#If Tokens have been created for this user
	if Tokens.query.filter_by(username=session['username']).first():
		#For each bank that we've stored tokens for
		resp_dict=[]
		for tokens in Tokens.query.filter_by(username=session['username']).all():
			#print('tokens.refresh_token='+tokens.refresh_token)
			resp_dict.append(json.loads(process_response(get_acct_url, tokens.access_token, tokens.refresh_token)))
		return render_template('accounts.html',title='Your Accounts', resp_dict=resp_dict)
	#Otherwise redirect to the truelayer connect to bank webpage and then return to original calling page
	else:
		session['return']='.get_acctinfo'
		return redirect(url_for('.truelayer'))

@app.route("/truelayer/accounts", methods=["GET"])
def get_accounts():
	"""Fetching a protected resource using an OAuth 2 token.
	"""
	#If Tokens have been created for this user
	if Tokens.query.filter_by(username=session['username']).first():
		data = get_balance_results()
		print(data)
		return render_template('balances.html',data=data)
	#Otherwise redirect to the truelayer connect to bank webpage and then return to original calling page
	else:
		session['return']='.get_accounts'
		return redirect(url_for('.truelayer'))

def get_balance_results():
		data=[]
		for x in session:
			print("session["+x+"]="+str(session[x]))
		if username in session:
			user=session['username']
		else:
			user=Deypay_user.query.filter_by(id=session['user_id']).first()
		print(user.username)
		#For each bank that we've stored tokens for this user
		for tokens in Tokens.query.filter_by(username=user.username).all():
			#print('access_token='+tokens.access_token)
			#print('refresh_token='+tokens.refresh_token)
			resp_dict=json.loads(process_response(get_acct_url, tokens.access_token, tokens.refresh_token))
			print("resp_dict:"+str(resp_dict))
			if 'error_description' in resp_dict:
					refresh_access_token(tokens.refresh_token)
			else:
				for results in resp_dict['results']:
					get_bal_url="https://api.truelayer.com/data/v1/accounts/"+results['account_id']+"/balance"
					bal_dict=json.loads(process_response(get_bal_url, tokens.access_token, tokens.refresh_token))
					data.append({"account":results, "balance":bal_dict['results'][0]})
		return data

@app.route("/truelayer/transactions", methods=["GET"])
def get_transactions():
	"""Fetching a protected resource using an OAuth 2 token.
	"""
	#If Tokens have been created for this user
	if Tokens.query.filter_by(username=session['username']).first():
		data=get_transaction_results()
		return render_template('transactions.html',data=data)
	#Otherwise redirect to the truelayer connect to bank webpage and then return to original calling page
	else:
		session['return']='.get_transactions'
		return redirect(url_for('.truelayer'))

def get_transaction_results():
	data=[]
	#For each bank that we've stored tokens for
	for tokens in Tokens.query.filter_by(username=session['username']).all():
		resp_dict=json.loads(process_response(get_acct_url, tokens.access_token, tokens.refresh_token))
		for results in resp_dict['results']:
			get_txn_url="https://api.truelayer.com/data/v1/accounts/"+results['account_id']+"/transactions"
			txn_dict=json.loads(process_response(get_txn_url, tokens.access_token, tokens.refresh_token))
			data.append({"account":results, "transactions":txn_dict['results']})	
	return data
	
# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404