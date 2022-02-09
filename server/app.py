from flask import Flask
from flask_cors import CORS

from blueprints.webui import templates_bp
from blueprints.api import api_bp


UPLOAD_FOLDER = 'blueprints/api/files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config.update(SECRET_KEY="2f7ac045-92d5-43d6-9d5b-ee068d4b9974")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FILE_NAME'] = 'event_log'

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
