from flask import Blueprint
from flask_cors import CORS

routes= Blueprint('routes', __name__) 
CORS(routes)


@routes.route("/")
def hello():
    return "Hello World!"
