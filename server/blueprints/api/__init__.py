# from crypt import methods
from importlib.resources import path
import json
import uuid
from os.path import join

from flask import Blueprint, send_file 
# from flask import flash

from flask import current_app
from flask import request
from flask import send_from_directory
# from flask import redirect
# from flask import url_for

# import process_eventlog


############################################################################
#   process.py module
############################################################################
#  Basic Dependences
import pm4py
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from os.path import dirname
from os.path import join

# from datetime import datetime

# from pm4py.util import constants

#  Realize importer/exportes to xes files
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter

#  Treat dataframes
from pm4py.objects.log.util import dataframe_utils

#  Convert dataframes to eventLogs
from pm4py.objects.conversion.log import converter as log_converter

#  Filters (EXTRA)
#  Filter to EventLogs
# from pm4py.algo.filtering.log.timestamp import timestamp_filter
# from pm4py.algo.filtering.log.cases import case_filter
#  Filter to  DATAFRAMES
# from pm4py.algo.filtering.pandas.timestamp import timestamp_filter as timestamp_filter_df
# from pm4py.algo.filtering.pandas.cases import case_filter as case_filter_df

#  DFG Algorithm
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization

############################################################################


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
            #  Generate SVG
            transform_csv_to_eventlog(file_name=file_name, folder_path=path)
            file_name_xes = f'{file_name[:-4]}.xes'
            transform_eventlog_to_dfg(file_name=file_name_xes, folder_path=path)
            
            return json.dumps({'message': 'File saved successfully', 
                               'status': 200,
                               'uri': f'{file_name_xes[:-4]}.svg'
                               })
        return json.dumps({'message': 'No content'})
    # return redirect(url_for('process'))


#  Calculate Rules
@api_bp.route('/get_data/<data_uri>', methods=['GET'])
def get_data(data_uri):
    # return send_from_directory(current_app.config['UPLOAD_FOLDER'], data_uri, as_attachment=True)
    path = join(current_app.config['UPLOAD_FOLDER'], data_uri)
    return send_file(path, mimetype='image/png')


#####################################################################################
#  process.py it causes error when importing :/
#####################################################################################

def transform_csv_to_eventlog(file_name:str, folder_path:str) -> None:
    #  Read file and create df
    path_csv = join(folder_path, file_name)
    log_csv_df = pd.read_csv(path_csv, 
                             sep=';', 
                             encoding='utf-8', 
                             dtype=str)
    log_csv_df = dataframe_utils.convert_timestamp_columns_in_df(log_csv_df)
    log_csv_df.columns = log_csv_df.columns.str.strip()
    log_csv_df = log_csv_df.sort_values('End')

    #  Create EventLog
    log_csv_df = pm4py.format_dataframe(df=log_csv_df, 
                                        case_id='Case',
                                        activity_key='ActivityCode',
                                        timestamp_key='End',
                                        start_timestamp_key='Start')
    log_csv = log_converter.apply(log_csv_df)

    #  Export EventLog
    path_xes = join(folder_path, f'{file_name[:-4]}.xes')
    xes_exporter.apply(log_csv, path_xes)

def transform_eventlog_to_dfg(file_name:str, folder_path:str) -> None:
    path_xes = join(folder_path, file_name)
    log_xes = xes_importer.apply(path_xes)
    dfg = dfg_discovery.apply(log_xes)
    gviz = dfg_visualization.apply(dfg, log=log_xes)
    path_svg = join(folder_path, f'{file_name[:-4]}.svg')
    dfg_visualization.save(gviz=gviz, 
                           output_file_path=path_svg)
    return
