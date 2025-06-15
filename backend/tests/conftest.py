import pytest
from config import create_app
from models.db import db_connect, metadata

@pytest.fixture(scope="session")
def engine_and_session():
    engine, SessionLocal = db_connect(testing=True)
    metadata.create_all(bind=engine)
    yield engine, SessionLocal
    metadata.drop_all(bind=engine)

@pytest.fixture
def app(engine_and_session):
    engine, SessionLocal = engine_and_session
    
    app = create_app(testing=True)
    
    @app.before_request
    def bind_test_session():
        from flask import g
        g.db_session = SessionLocal()
    
    @app.teardown_request
    def remove_session(exception=None):
        from flask import g
        if hasattr(g, 'db_session'):
            g.db_session.close()
        
    yield app

def client(app):
    return app.test_client()