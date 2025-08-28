from config import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.secret_key = os.getenv("SECRET_KEY")
    app.run(debug=True)