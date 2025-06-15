from flask import request, Blueprint, jsonify
from werkzeug.security import check_password_hash
from api.api_user import getUserById

read_blueprint = Blueprint("read", __name__)

@read_blueprint.route("/user/<int:user_id>", methods=["GET"])
async def read(user_id):
    user = await getUserById(user_id)
    
    if user:
        user_info = {
            "user_name" : user.user_name
        }
        
        return jsonify(user_info), 200
    
    else:
        return jsonify(f"Havent user with this id:{user_id}"), 404