import pytest
from config import create_app
from models.db import db_connect, metadata

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

    @app.before_request
    def inject_session():
        from flask import g
        g.db_session = db_session

    yield app
        

@pytest.fixture
def client(app):
    return app.test_client()