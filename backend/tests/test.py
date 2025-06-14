import pytest
from flask import Flask
from models.db import Base
from main import app
from models.user import User
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def test_app():
    app = Flask(__name__)
        