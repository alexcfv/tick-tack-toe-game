from flask import g, Flask
from flask_cors import CORS
from models.db import db_connect

def create_app(testing=False):
    app = Flask("main")
    CORS(app)
    
    engine, SessionLocal = db_connect(testing=testing)
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db = g.pop('db_session', None)
        if db is not None:
            db.close()

    @app.before_request
    def create_session():
        g.db_session = SessionLocal()
        
    return app