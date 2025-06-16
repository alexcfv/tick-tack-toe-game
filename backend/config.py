from flask import g, Flask
from flask_cors import CORS
from models.db import db_connect
from handlers.user.registration import registration_blueprint
from handlers.user.login import login_blueprint
from handlers.user.delete import delete_blueprint
from handlers.user.update import update_blueprint
from handlers.user.read import read_blueprint
from handlers.game.game import game_blueprint
from models.user_login import UserLogin
from flask_login import LoginManager
from limiting import limiting_remote_addr

def create_app(testing=False):
    app = Flask("main")
    CORS(app)
    
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return UserLogin().fromBD(user_id)

    app.register_blueprint(registration_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(delete_blueprint)
    app.register_blueprint(update_blueprint)
    app.register_blueprint(read_blueprint)
    app.register_blueprint(game_blueprint)
    
    app.before_request(limiting_remote_addr)
    
    engine, SessionLocal = db_connect(testing=testing)
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db = g.pop("db_session", None)
        if db is not None:
            db.close()

    @app.before_request
    def create_session():
        g.db_session = SessionLocal()
        
    return app