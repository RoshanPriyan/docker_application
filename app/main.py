from flask import Flask
from dotenv import load_dotenv
import os
from router import api_route as user
from config import DATABASE_URL

load_dotenv()

host = os.getenv("FLASKHOST")
port = os.getenv("FLASKPORT")
debug = os.getenv("FLASKDEBUG")

app = Flask(__name__)

@app.route('/')
def starting():
    print('Application Starting ....')
    return "Applicatioin Starting..."

print(DATABASE_URL)
app.register_blueprint(user, url_prefix="/api/user")

if __name__ == "__main__":
    app.run(host=host,port=port, debug=debug)