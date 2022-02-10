import json
import uuid
from os.path import join

from flask import request
from flask import Blueprint, send_file

from flask import current_app

from .process import transform_csv_to_eventlog, transform_eventlog_to_dfg, create_data_dir, create_new_file_extension


api_bp = Blueprint('api', __name__)


@api_bp.route('/post_data', methods=["POST"])
def post_data():
    """
    Generate the .xes and .svg files from the csv data uploaded.
    Save files to a local /data directory. the /data directory is created
    if not present.
    """
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
            file_name_svg = create_new_file_extension(file_name, extension='.svg')
            return json.dumps({'message': 'File saved successfully',
                               'status': 200,
                               'uri': file_name_svg
                               })
        return json.dumps({'message': 'No content'})


#  Calculate Rules
@api_bp.route('/get_data/<data_uri>', methods=['GET'])
def get_data(data_uri):
    path = join(current_app.config['UPLOAD_FOLDER'], data_uri)
    return send_file(path, mimetype='image/png')
