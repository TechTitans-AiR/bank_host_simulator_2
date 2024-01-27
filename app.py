from flask import Flask
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://tsopic:LeTEhX16v0tdIRW9@cluster0.uc4rj5a.mongodb.net/transaction_management' 

mongo = PyMongo(app)

from controllers.CardsController import cards_controller_bp
app.register_blueprint(cards_controller_bp)


if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088, debug = False)
