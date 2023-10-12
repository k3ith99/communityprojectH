from flask import Flask
from flask_cors import CORS
from os import path
from flask_jwt_extended import JWTManager
from .Routes import routes

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #add db init and auth here
    app = Flask(__name__)
    JWTManager(app)


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
            populate_database_with_users()

            print('Created Database!')
def populate_database_with_users():
    # Check if a user with the same email already exists
    existing_user = Users.query.filter_by(email='john@example.com').first()

    if not existing_user:
        # Create and add the user to the session
        user1 = Users(
            firstname='John',
            surname='Doe',
            email='john@example.com',
            password='password1',
            address='123 Main St'
        )
        db.session.add(user1)
        db.session.commit()
    else:
        print(f"User with email 'john@example.com' already exists.")


