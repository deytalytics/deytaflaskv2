from app import app
from flask_cors import CORS
application = CORS(app)
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000)