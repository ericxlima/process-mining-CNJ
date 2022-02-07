from flask import Blueprint

from flask import request
from flask import redirect
from flask import url_for

api_bp = Blueprint('api', __name__,
                   static_folder='./server/static')

@api_bp.route('/')
def index_api():
    return '<h1>Bem vindo a API</h1>'


#  Get csv file from FrontEnd
@api_bp.route('/post_data', methods=["POST"])
def post_data():
    uploaded_file = request.files['file']
    if uploaded_file:
        # set the file path
        uploaded_file.save("./files")
        # save the file
    return redirect(url_for('process'))

#  Calculate Rules
@api_bp.route('/process')
def process():
    #  Transform csv in xes (eventlog)
    return 'Você conseguiu! XD'
