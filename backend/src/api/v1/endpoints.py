from flask import Blueprint, Response
import logging
from flask import Flask, jsonify, request

# import os
# from datetime import datetime
# from flask import send_file, request
# from werkzeug.security import check_password_hash
# from flask_jwt_extended import create_access_token, jwt_required

from utils import banks
from utils import ml

log = logging.getLogger("endpoints-logger")

# Create a Blueprint for the API version
v1_blueprint = Blueprint("v1", __name__)


@v1_blueprint.route("/", methods=["GET"])
def home():
    log.debug("root endpoint was called.")
    return jsonify({"response": "Hello from SchuFHEr backend!"})


@v1_blueprint.route("/auth", methods=["POST"])
def validate_password():
    log.debug("Authentification initiated.")
    # # Get the password from request body
    # password = request.get_json().get('password')
    # hashed_password = os.getenv('__TESTUSER_PWD__')

    # # Get the valid password from docker container
    # if check_password_hash(hashed_password, password):
    #     # Generate JWT token.
    #     access_token = create_access_token(identity='user')
    #     log.debug("Authentification successful.")
    #     return jsonify(access_token=access_token), 200
    # else:
    #     log.debug("Authentification failed.")
    #     return jsonify({'authenticated': False}), 401


@v1_blueprint.route("/banks", methods=["GET"])
def get_banks():
    log.debug("Get banks endpoint was called.")
    return jsonify(banks.get_banks_for_user(request.get_json().get("uid")))


@v1_blueprint.route("/submit", methods=["POST"])
def submit_rating():
    """
    Submit a rating from a bank.    
    { immo, accounts, credits, nonpayments, creditcards, living }
    """
    ml.add_to_state(request.get_json().get("id"), request.get_json().get("submission"))
    return jsonify({"response": "Rating submitted!"}), 200


@v1_blueprint.route("/get_score", methods=[ "GET"])
def get_score():
    return jsonify({"score": ml.predict_score(0)}), 200
