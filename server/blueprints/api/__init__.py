from urllib import response
from flask import Blueprint

from flask import request
from flask import redirect
from flask import url_for

api_bp = Blueprint('api', __name__,
                   static_folder='./server/static')

@api_bp.route('/')
def index_api():
    return '<h1>Wellcome to API</h1>'


#  Get csv file from FrontEnd
@api_bp.route('/post_data', methods=["POST"])
def post_data():
    header = request.headers
    header['Access-Control-Allow-Origin'] = '*'
    return '', 200
    file = request.files.get('file')
    print(file)
    if uploaded_file:
        uploaded_file.save("./files")
    # return redirect(url_for('process'))


#  Calculate Rules
@api_bp.route('/process')
def process():
    #  Transform csv in xes (eventlog)
    return 'Well Done! XD'
