from flask import request, Blueprint, jsonify
from werkzeug.security import check_password_hash
from api.api_user import getUser, deleteUserById
from flask_login import login_required

delete_blueprint = Blueprint("delete", __name__)

@delete_blueprint.route("/delete", methods=["POST"])
@login_required
async def delete():
    user = request.get_json()
    
    try:
        user_name = user["user_name"]
    except:
        return "Must have user_name", 400
    
    if type(user_name) != str:
        return jsonify("Uncorrect user name"), 422
    
    user_from_bd = await getUser(user_name)
    
    if user_from_bd and user_from_bd.user_name == user_name:
        user_id = user_from_bd.id
        result = await deleteUserById(user_id)
        if result: return jsonify("Succesful delete"), 204
    
    else:
        return jsonify("Have not user"), 400