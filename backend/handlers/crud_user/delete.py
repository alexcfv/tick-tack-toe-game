from flask import request, Blueprint, jsonify
from werkzeug.security import check_password_hash
from api.api_user import getUser, deleteUserById

delete_blueprint = Blueprint("delete", __name__)

@delete_blueprint.route("/delete", methods=["POST"])
async def delete():
    user = request.get_json()
    user_name = user["user_name"]
    
    user_from_bd = await getUser(user_name)
    
    if user_from_bd:
        user_id = user_from_bd.id
        result = await deleteUserById(user_id)
        if result: return "Succesful delete"
    
    else:
        return "Have not user"