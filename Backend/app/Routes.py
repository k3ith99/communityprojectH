from flask import Blueprint,request, jsonify, Flask
from flask_cors import CORS
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, get_jwt_identity, decode_token, JWTManager, get_jwt
from datetime import timedelta
from .Models import Users
from .Config import db
from blocklist import BLOCKLIST



routes= Blueprint('routes', __name__) 
CORS(routes)
jwt = JWTManager()


@routes.route("/")
def hello():
    return "Hello World!"



@routes.route("/register", methods = ['POST'])
def register():
    req = request.get_json()
    hashed_password = generate_password_hash(req['password'])
    user = Users.query.filter_by(email=req['email']).first()
    if not user:
        new_user = Users(
            firstname= req['firstname'], 
            surname= req['surname'], 
            email= req['email'], 
            password= hashed_password, 
            address= req['address'])
        db.session.add(new_user)
        db.session.commit()
        return f"New user was registered", 201
    else:
        return f"User already exists", 409



#remember to store access token on client side
@routes.route("/login",methods = ['POST'])
def login():
    req = request.get_json()
    #check if user exists
    user = Users.query.filter_by(email=req['email']).first()
    if user:
        print(f"{user.email}")
        #check if password is correct
        if check_password_hash(user.password, req['password']):
            access_token = create_access_token(identity=user.email,expires_delta=timedelta(minutes=30))
            refresh_token = create_refresh_token(identity= user.email,expires_delta=timedelta(minutes=30))
            return (
                    {"access_token": access_token,
                    "refresh_token": refresh_token
                    }
            ),201
        else:
            return f"Login failed, password is wrong", 401 
    else:
        return f"Login failed, user does not exist", 401
    #if both conditions are satisfied create a token




#Access user info
@routes.route("/account", methods = ['GET'])
@jwt_required()
def account():
    current_user = get_jwt_identity()
    user = Users.query.filter_by(email=current_user).first()
    return {
        "id": user.id,
        "firstname": user.firstname,
        "surname": user.surname,
        "email": user.email,
        "address": user.address
    }


# Function to add a token's JTI to the blocklist
def revoke_token(jti):
    BLOCKLIST.add(jti)

# Function to check if a token is revoked
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in BLOCKLIST

#Route to revoke a token
#clear cookies on server side in order to implement logout
@routes.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    revoke_token(jti)
    return jsonify(message='Access token has been revoked'), 200



@routes.route('/forgot-password', methods=['PATCH', 'PUT'])
@jwt_required()
def forgot_password():
    current_user = get_jwt_identity()
    req = request.get_json()
    user = Users.query.filter_by(email=current_user).first()
    hashed_password = generate_password_hash(req['password'],method='pbkdf2:sha256')
    user.password = hashed_password
    db.session.commit()
    return "Password has been updated succesfully", 200


@routes.route('/delete-account',methods = ['DELETE'])
@jwt_required()
def delete_account():
    current_user = get_jwt_identity()
    user = Users.query.filter_by(email=current_user).first()
    db.session.delete(user)
    db.session.commit()
    return f"User has been deleted successfully",200
