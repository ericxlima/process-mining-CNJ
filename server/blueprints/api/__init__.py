# from crypt import methods
import json
import uuid
from os.path import join

from flask import Blueprint 
# from flask import flash

from flask import current_app
from flask import request
from flask import send_from_directory
# from flask import redirect
# from flask import url_for

# import process_eventlog


api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def index_api():
    body = '<h1>Wellcome to API</h1>'
    return body


#  Get csv file from FrontEnd
@api_bp.route('/post_data', methods=["POST"])
def post_data():
    if request.method == 'POST':
        if request.data:
            path = current_app.config['UPLOAD_FOLDER']
            file_name = f"{current_app.config['FILE_NAME']}.{uuid.uuid4().hex}.csv"
            with open(join(path, file_name), 'wb') as uploaded_file:
                uploaded_file.write(request.data)
            return json.dumps({'message': 'File saved successfully', 'status': 200})
        return json.dumps({'message': 'No content'})
    # return redirect(url_for('process'))


#  Calculate Rules
@api_bp.route('/process')
def process():
    #  Transform csv in xes (eventlog)
    return 'Well Done! XD'
