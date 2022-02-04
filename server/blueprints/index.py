from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/')
def index():
    return "I am alive"