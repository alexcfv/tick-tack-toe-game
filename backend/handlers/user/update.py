from flask import request, Blueprint, jsonify
from api.api_user import updateUserById, getUser
from flask_login import login_required
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

update_blueprint = Blueprint("update", __name__)

@update_blueprint.route("/update", methods=["POST"])
@login_required
async def update():
    user = request.get_json()
    try:
        user_name = user["user_name"]
        user_password = user["password"].strip()
        new_user_password = user["new_password"]
    except:
        return "Must have user_name, password and new_password", 400
    
    user_from_bd = await getUser(user_name)
    
    if user_from_bd:
        if check_password_hash(user_from_bd.password, user_password):
            
            new_user_info = User(
                user_name=user_name,
                password = generate_password_hash(new_user_password)
            )
        
            user_id = user_from_bd.id
        
            result = updateUserById(user_id=user_id, data=new_user_info)
        
            if result: return jsonify("Update succesful"), 200
            else: return jsonify("Error"), 400
        else:
            return "Uncorrect password", 400
    else:
        return jsonify("Uncorrect password"), 400