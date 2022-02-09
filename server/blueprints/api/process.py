#  Basic Dependences
import pm4py
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

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


PATH_FILE_XES = 'blueprints/api/files/EventLog_Anonim_UTF8.xes'
PATH_FILE_CSV = 'blueprints/api/files/EventLog_Anonim_UTF8.csv'
PATH_FILE_SVG = 'blueprints/api/files/EventLog_Anonim_UTF8.svg'


def transform_csv_to_eventlog():
    #  Read file and create df
    log_csv_df = pd.read_csv(PATH_FILE_CSV, 
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
    xes_exporter.apply(log_csv, PATH_FILE_XES)

def transform_eventlog_to_dfg():
    log_xes = xes_importer.apply(PATH_FILE_XES)
    dfg = dfg_discovery.apply(log_xes)
    gviz = dfg_visualization.apply(dfg, log=log_xes)
    dfg_visualization.save(gviz=gviz, output_file_path=PATH_FILE_SVG)
    return


#  Aply Filters...
def filters():
    """TO DO..."""
    return


if __name__ == '__main__':
    transform_csv_to_eventlog()
    transform_eventlog_to_dfg()
