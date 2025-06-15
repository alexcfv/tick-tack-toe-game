from config import create_app
from handlers.crud_user.registration import registration_blueprint
from handlers.crud_user.login import login_blueprint
from handlers.crud_user.delete import delete_blueprint
from handlers.crud_user.update import update_blueprint
from models.user_login import UserLogin
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromBD(user_id)

app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(delete_blueprint)
app.register_blueprint(update_blueprint)

if __name__ == "__main__":
    app.secret_key = os.getenv("SECRET_KEY")
    app.run(debug=True)