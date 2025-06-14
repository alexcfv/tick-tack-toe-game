from flask import request, Blueprint
from api.api_user import updateUserById, getUserById
from flask_login import login_required
from models.user import User
from models.user_login import UserLogin
from werkzeug.security import generate_password_hash, check_password_hash

update_blueprint = Blueprint("update", __name__)

@update_blueprint.route("/update", methods=["POST"])
@login_required
async def update():
    user = request.get_json()
    user_name = user["user_name"]
    user_password = user["password"]
    
    user_from_bd = await getUserById(int(UserLogin.get_id()))
    
    if user_from_bd:
        if check_password_hash(user_from_bd.password, user_password):
            
            new_user_password = user["new_password"]
            
            new_user_info = User(
                user_name=user_name,
                password = generate_password_hash(new_user_password)
            )
        
            user_id = user_from_bd.id
        
            result = updateUserById(user_id=user_id, data=new_user_info)
        
            if result: return "Update succesful"
            else: return "Error"
    else:
        return "Uncorrect password"