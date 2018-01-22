import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app_config = os.getenv("APP_CONFIG")
app.config.from_object(app_config)
# CORS(app, resources={r"/*": {"origins": app.config["CORS_ALLOWED_ORIGINS"]}})
CORS(app, resources={r"/*": {"origins": "*"}})

from .control import *

if __name__ == "__main__":
    app.run(host="0.0.0.0")
