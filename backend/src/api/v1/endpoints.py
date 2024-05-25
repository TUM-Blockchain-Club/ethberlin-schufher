from flask import Blueprint, Response
import logging
from flask import Flask, jsonify, request
from utils import institutions

# from utils import ml

log = logging.getLogger("endpoints-logger")
v1_blueprint = Blueprint("v1", __name__)


@v1_blueprint.route("/", methods=["GET"])
def home():
    log.debug("root endpoint was called.")
    return jsonify({"response": "Hello from SchuFHEr backend!"})


@v1_blueprint.route("/institutions", methods=["GET"])
def get_banks():
    log.debug("Get institutions endpoint was called.")
    return jsonify(institutions.get_insts_for_user(request.args.get("uid")))


@v1_blueprint.route("/submit", methods=["POST"])
def submit_rating():
    """
    Submit an encrypted rating from a bank.
    """
    # ml.add_to_state(request.get_json().get("id"), request.get_json().get("submission"))
    return jsonify({"response": "Rating submitted!"}), 200


#
# this functionality doesn't work on apple silicon :(
#
# @v1_blueprint.route("/get_score", methods=[ "GET"])
# def get_score():
#     return jsonify({"score": ml.predict_score(0)}), 200
