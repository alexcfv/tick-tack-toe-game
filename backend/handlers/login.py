from flask import request, Blueprint, jsonify
from werkzeug.security import check_password_hash
from api.api_user import getUser
from models.user_login import UserLogin
from flask_login import login_user

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/login", methods=["POST"])
async def login():
    logging_user = request.get_json()
    logging_user_password = logging_user["password"]
    logging_user_name = logging_user["user_name"]
    
    user_from_bd = await getUser(logging_user_name)
    
    if user_from_bd:
        hash = user_from_bd.password
        
        if check_password_hash(hash, logging_user_password):
            userlogin = UserLogin().create(user_from_bd)
            login_user(userlogin)
            return jsonify(True)
        else:
            return jsonify(False)
    else:
        return jsonify(False)