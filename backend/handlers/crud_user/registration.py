from flask import request, Blueprint, jsonify
from werkzeug.security import generate_password_hash
from api.api_user import addUser, getUser

registration_blueprint = Blueprint("registration", __name__)

@registration_blueprint.route("/registration", methods=["POST"])
async def registration():
    registing_user = request.get_json()
    registing_user_name = registing_user["user_name"]
    
    registing_user_password = registing_user["password"]
    
    if len(registing_user_name) > 4  and len(registing_user_name) < 20 \
        and len(registing_user_password) > 4 and len(registing_user_password) < 20:
                
        hash = generate_password_hash(registing_user_password)
        result = await addUser(registing_user_name, hash)
    
    if result: return "Registration succesful"
    else: return "Eror"