import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import CORS
from .routes.main import bp as main
from .routes.users import bp_users
from .models import db
from .models.user import User

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = os.getenv("DEBUG", False)
app.config['ENV'] = os.getenv("ENV", "production")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if os.getenv("DEBUG"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("EXTERNAL_DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("INTERNAL_DATABASE_URL")

db.init_app(app)
Migrate(app, db)
CORS(app)

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