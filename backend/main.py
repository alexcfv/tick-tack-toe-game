from flask import Flask
from flask_cors import CORS
from handlers.registration import registration_blueprint
from handlers.login import login_blueprint
from handlers.delete import delete_blueprint
from models.user_login import UserLogin
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromBD(user_id)

app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(delete_blueprint)

if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True)