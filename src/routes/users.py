from flask import Blueprint, request, jsonify, abort

bp_users = Blueprint("bp_users", __name__)
@bp_users.route('/test')
@bp_users.route('/test/<username>')
def test(username=None):
    if username is None:
        abort(400, "username is required")

    return jsonify({ "route": "test" }), 200