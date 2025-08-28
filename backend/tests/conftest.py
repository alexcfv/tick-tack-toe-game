import pytest
from config import create_app
from models.db import db_connect
from models.user_login import UserLogin
from models.user import User
from flask_login import login_user

@pytest.fixture(scope="session")
def db_session():
    engine, SessionLocal = db_connect(testing=True)
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def app(db_session):
    app = create_app(testing=True)
    app.secret_key ="test_secret_key"

    @app.before_request
    def inject_session():
        from flask import g
        g.db_session = db_session

    yield app
        

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def login_user_fixture(app):
    with app.test_request_context():
        user = User(
            id = 2,
            user_name = "Valid name",
            password = "Valid password"
        )
        
        user = UserLogin().create(user)
        
        login_user(user)
        yield user