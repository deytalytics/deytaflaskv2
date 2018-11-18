from app import app
from flask_cors import CORS
application = CORS(app)
if __name__ == '__main__':
	context = ('deytalytics-le.crt', 'deytalytics-private.key')
	#app.run(ssl_context=context)
	app.run()