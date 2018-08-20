name = "table_describer"

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

import pandas as pd
import numpy as np

'''
A rough script to wrangle data characteristics
out of unstructured data before trying to load
into a structured database or the like
'''


def describe_csv(input_table, date_fields=[]):
    '''
    print some details to screen about
    a provided csv file

    @params: 
      input_table: string filepath to a csv file
      date_fields: list of fields that should be of type 'timestamp'
    '''

    # Load input data into panda data frame
    df_input = pd.read_csv(input_table)

    # create 2nd data frame from data structure
    df = pd.DataFrame.from_dict(data=dict(df_input.dtypes),
                                orient="index",
                                columns=["NumpyType"])
    df.index.name = "FieldName"

    # Do we have datetime fields? If so, convert them here:
    for f in date_fields:
        try:
            df_input[f] = pd.to_datetime(df_input[f])
            df.loc[df.index == f, "NumpyType"] = np.dtype('M')
        except ValueError as e:
            print "%s had unparseable values for datetime." % f

    # get length of string fields and update data type to include this:
    df['DataType'] = df["NumpyType"]
    df['IsUnique'] = ""
    for i in df.index:
        if df.loc[i].DataType.name == 'object':
            df.DataType[i] = "string(%i)" % df_input[i].str.len().max()
        df.IsUnique[i] = df_input[i].is_unique
    print "SCHEMA INFO"
    print df
    print "DATA CHARACTERISTICS"
    print df_input.describe().round()
