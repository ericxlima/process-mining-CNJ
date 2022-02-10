from pathlib import Path
from os.path import exists
from os import mkdir

from flask import current_app

import pm4py
import pandas as pd

from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization


def create_data_dir():
    """
    Create /data directory for holding generated files.
    """
    if not exists(current_app.config['UPLOAD_FOLDER']):
        mkdir(current_app.config['UPLOAD_FOLDER'])


def transform_csv_to_eventlog(file_path: str) -> None:
    #  Read file and create df
    log_csv_df = pd.read_csv(
        file_path,
        sep=';',
        encoding='utf-8',
        dtype=str
    )
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

    # Export EventLog
    renamed_file_path = create_new_file_extension(file_path)
    xes_exporter.apply(log_csv, renamed_file_path)

    transform_eventlog_to_dfg(renamed_file_path)


def transform_eventlog_to_dfg(file_path: str) -> None:
    log_xes = xes_importer.apply(file_path)
    dfg = dfg_discovery.apply(log_xes)
    gviz = dfg_visualization.apply(dfg, log=log_xes)

    new_svg_path = create_new_file_extension(file_path, extension='svg')
    dfg_visualization.save(gviz=gviz,
                           output_file_path=new_svg_path)


def create_new_file_extension(file_path: str, extension: str = '.xes') -> str:
    if '.' not in extension:
        extension = f'.{extension}'

    local_path = Path(file_path)
    renamed_file_path = str(local_path.with_suffix(extension))
    return renamed_file_path
