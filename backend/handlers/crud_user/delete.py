from flask import request, Blueprint, jsonify
from werkzeug.security import check_password_hash
from api.api_user import getUserById, deleteUserById
from flask_login import login_required
from models.user_login import UserLogin

delete_blueprint = Blueprint("delete", __name__)

@delete_blueprint.route("/delete", methods=["POST"])
@login_required
async def delete():
    user = request.get_json()
    user_name = user["user_name"]  
    user_from_bd = await getUserById(int(UserLogin.get_id()))
    
    if user_from_bd and user_from_bd.user_name == user_name:
        user_id = user_from_bd.id
        result = await deleteUserById(user_id)
        if result: return "Succesful delete"
    
    else:
        return "Have not user"