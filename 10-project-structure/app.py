from flask import Flask
from routes.main import register_routes

app = Flask(__name__)

register_routes(app)


if __name__ == "__main__":
    app.run(debug=True)