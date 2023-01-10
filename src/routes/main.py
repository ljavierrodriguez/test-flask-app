from flask import Blueprint, jsonify

bp = Blueprint("bp", __name__)

@bp.route('/')
def main():
    return jsonify({ "msg": "Welcome to Fist Rest API with Flask" }), 200