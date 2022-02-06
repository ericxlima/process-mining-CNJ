from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "hello"

@app.route('/api/v1/load_data', methods=["POST"])
def load_data():
    body = request.get_csv()
    print(body)
    
    return body


