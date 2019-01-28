from app import app
from flask_cors import CORS
application = CORS(app)
if __name__ == '__main__':
	app.run()