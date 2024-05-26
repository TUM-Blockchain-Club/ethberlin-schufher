from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from src.api.v1.endpoints import v1_blueprint
from src.utils.logger import Logger

# Init flask app
app = Flask(__name__)
CORS(app)

app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

# Init JWT manager
# app.config['JWT_SECRET_KEY'] = os.environ['__JWT_SECRET_KEY__']
# jwt = JWTManager(app)

# Initialize logger
Logger.init_logger()

if __name__ == "__main__":
    app.run(debug=True)
