from flask import Blueprint


api_bp = Blueprint('api', __name__,
                   static_folder='./server/static')

@api_bp.route('/')
def index_api():
    return '<p>Bem vindo a API</p>'

