from flask import Flask
from flask_cors import CORS

from blueprints.webui import templates_bp
from blueprints.api import api_bp


app = Flask(__name__)
app.config.update(SECRET_KEY="123456789")

CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins": "*",
        # "origins": "localhost",
    }
})

# app.config["DEBUG"] = True

app.register_blueprint(templates_bp)
app.register_blueprint(api_bp, url_prefix='/api/v1')
