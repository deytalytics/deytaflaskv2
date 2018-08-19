from app import app
application = app
if __name__ == '__main__':
	context = ('deytalytics.crt', 'deytalytics.key')
	app.run(ssl_context=context)