import pm4py
import pandas as pd

#  Realize importer/exportes to xes files
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter

#  Treat dataframes
from pm4py.objects.log.util import dataframe_utils

#  Convert dataframes to eventLogs
from pm4py.objects.conversion.log import converter as log_converter

#  Filter to timestamps/cases
from pm4py.algo.filtering.log.timestamp import timestamp_filter
from pm4py.algo.filtering.log.cases import case_filter

#  Filter to timestamps/cases IN DATAFRAMES
from pm4py.algo.filtering.pandas.timestamp import timestamp_filter as timestamp_filter_df
from pm4py.algo.filtering.pandas.cases import case_filter as case_filter_df


PATH_FILE_XES = 'blueprints/api/files/EventLog_Anonim_UTF8.xes'
PATH_FILE_CSV = 'blueprints/api/files/EventLog_Anonim_UTF8.csv'


def transform_csv_to_eventlog():
    #  Read file and create df
    log_csv_df = pd.read_csv(PATH_FILE_CSV, sep=';', encoding='utf-8')
    log_csv_df = dataframe_utils.convert_timestamp_columns_in_df(log_csv_df)
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