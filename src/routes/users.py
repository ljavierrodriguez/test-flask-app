from flask import Blueprint, request, jsonify, abort
from src.models.user import User

bp_users = Blueprint("bp_users", __name__)
@bp_users.route('/test')
@bp_users.route('/test/<username>')
def test(username=None):
    if username is None:
        abort(400, "username is required")

    return jsonify({ "route": "test" }), 200


@bp_users.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200