from flask import Blueprint, request, jsonify

bp_users = Blueprint("bp_users", __name__)
@bp_users.route('/test')
def test():
    return jsonify({ "route": "test" }), 200