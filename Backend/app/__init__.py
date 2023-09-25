from flask import Flask
from .Routes import routes

def create_app():
    #add db init and auth here
    app = Flask(__name__)
    app.register_blueprint(routes)

    return app
