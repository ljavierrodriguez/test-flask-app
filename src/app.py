import os
from flask import Flask
from dotenv import load_dotenv
from routes.main import bp as main

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = os.getenv("DEBUG", False)
app.config['ENV'] = os.getenv("ENV", "production")

app.register_blueprint(main)


if __name__ == '__main__':
    app.run()