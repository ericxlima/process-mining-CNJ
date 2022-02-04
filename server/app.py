from flask import Flask
from server.blueprints.index import index

app = Flask(__name__)
app.register_blueprint(index)

