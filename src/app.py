import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from .routes.main import bp as main
from .routes.users import bp_users

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = os.getenv("DEBUG", False)
app.config['ENV'] = os.getenv("ENV", "production")

app.register_blueprint(main)
app.register_blueprint(bp_users, url_prefix="/api")


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(error=str(ex)), ex.code
    else:
        return jsonify(error=str(ex)), ex.code


@app.errorhandler(400)
def _handle_api_error(ex):
    return jsonify(error=str(ex)), ex.code