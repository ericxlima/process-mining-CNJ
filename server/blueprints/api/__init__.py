import json
import uuid
from os.path import join

from flask import request
from flask import Blueprint, send_file

from flask import current_app

from .process import transform_csv_to_eventlog, transform_eventlog_to_dfg, create_data_dir


api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def index_api():
    body = '<h1>Wellcome to API</h1>'
    return body


#  Get csv file from FrontEnd
@api_bp.route('/post_data', methods=["POST"])
def post_data():
    if request.method == 'POST':
        create_data_dir()
        if request.data:
            path = current_app.config['UPLOAD_FOLDER']
            file_name = f"{current_app.config['FILE_NAME']}.{uuid.uuid4().hex}.csv"
            file_path = join(path, file_name)
            with open(file_path, 'wb') as uploaded_file:
                uploaded_file.write(request.data)
            #  Generate SVG
            transform_csv_to_eventlog(file_path)
            file_name_xes = f'{file_name[:-4]}.xes'

            return json.dumps({'message': 'File saved successfully', 
                               'status': 200,
                               'uri': f'{file_name_xes[:-4]}.svg'
                               })
        return json.dumps({'message': 'No content'})
    # return redirect(url_for('process'))


#  Calculate Rules
@api_bp.route('/get_data/<data_uri>', methods=['GET'])
def get_data(data_uri):
    path = join(current_app.config['UPLOAD_FOLDER'], data_uri)
    return send_file(path, mimetype='image/png')
