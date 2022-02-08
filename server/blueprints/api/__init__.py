from flask import Blueprint, flash

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
    if request.method == 'POST':
        if 'file' not in request.files:
            # flash('No file ;-;', 'warning')
            print('<oh no, this is not a file>')
            return ';-;'
        
        file = request.files.get('file')
        print(file)
        if file:
            file.save(f"blueprints/api/files/{file.filename}.csv")
            print('<ohh yeah>')
            return 'Well Done', 200
        return 'No selected File'
        # return redirect(url_for('process'))


#  Calculate Rules
@api_bp.route('/process')
def process():
    #  Transform csv in xes (eventlog)
    return 'Well Done! XD'
