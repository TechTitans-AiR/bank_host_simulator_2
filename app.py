from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

from controllers.CardsController import cards_controller_bp
app.register_blueprint(cards_controller_bp)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8088, debug = False)
