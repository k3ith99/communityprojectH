from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path

from .Routes import routes
from .itinerary import itinerary

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #add db init and auth here
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(itinerary, url_prefix='/itinerary')

    create_database(app)

    return app

def create_database(app):
    if not path.exists('./server/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')