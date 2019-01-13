#!/usr/bin/env python
# created by rsutcliffe 20190106
name = "table_describer"

from warnings import filterwarnings, simplefilter
filterwarnings("ignore", message="numpy.dtype size changed")
filterwarnings("ignore", message="numpy.ufunc size changed")
simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import numpy as np
import argparse

'''
A rough script to wrangle data characteristics
out of unstructured data before trying to load
into a structured database or the like
'''


def describe_csv(input_table, date_fields=[], schema=True,
                 characteristics=True, uniqueness=True):
    '''
    print some details to screen about
    a provided csv file

    @params:
      input_table: string filepath to a csv file
      date_fields: list of fields that should be of type 'timestamp'
      schema = report on schema (default=True)
      characteristics = report on data characteristics (default=True)
      uniqueness = report on data uniqueness (default=True)

    :return dict with schema, characteristics, and uniqueness keys (each a dataframe)
    '''

    # Load input data into panda data frame
    if len(date_fields) > 0:
        # If user specified date fields, convert them:
        df_input = pd.read_csv(input_table, parse_dates=date_fields)
    else:
        # otherwise take best shot at identifying date fields
        # this doesn't seem to find many datetime fields I've seen...
        df_input = pd.read_csv(input_table, parse_dates=True)
    results = {}
    if schema:
        # create 2nd data frame from data structure for schema

        df = pd.DataFrame.from_dict(data=dict(df_input.dtypes),
                                    orient="index",
                                    columns=["NumpyType"])
        df.index.name = "FieldName"

        # get length of string fields and update data type to include this:
        df['DataType'] = df["NumpyType"]
        df['IsUnique'] = ""
        for i in df.index:
            if df.loc[i].DataType.name == 'object':
                df.DataType[i] = "string(%i)" % df_input[i].str.len().max()
            df.IsUnique[i] = df_input[i].is_unique
        results["schema"] = df
    if characteristics:
        # get characteristics of table via table describe:
        results["characteristics"] = df_input.describe().round()

    if uniqueness:
        # look at each field and report on the uniqueness of their values:
        results["uniqueness"] = getuniqueness(df_input)

    return results


def getuniqueness(df_input):
    '''

    :param df_input: input_dataframe
    :return: dataframe with min,max,avg of unique values in each field
    '''

    df = pd.DataFrame(columns=['field', 'totalvals', 'totaluniquevals', 'min_occ', 'max_occ', 'avg_occ'])
    for i in df_input.columns.values:

        x = {}
        x["field"] = i
        x["totalvals"] = df_input[i].count()
        x["totaluniquevals"] = len(df_input[i].unique())
        x["min_occ"] = (min(df_input[i].value_counts()))
        x["max_occ"] = max(df_input[i].value_counts())
        x["avg_occ"] = round(__mean(df_input[i].value_counts()), 0)
        df = df.append(x, ignore_index=True)

    return df


def __mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def main():
    # Command Line utility:
    parser = argparse.ArgumentParser(prog="Table Describer",
                                     description="Print characteristics of a table schema",
                                     epilog="Example: tbl_desc 'c:/data/mytable.csv'")
    parser.add_argument("inputtable", help="<Required> the full path to the table to describe.")
    parser.add_argument("-d", "--datefields", nargs='*',
                        help="<Required>r the field(s) that are date timestamps and should be treated as such, "
                             "not as number values")
    args = parser.parse_args()

    input_tbl = args.inputtable.replace("'","").replace('"','')
    if args.datefields:
        date_fields = ['{0}'.format(s).replace("'","") for s in args.datefields]  # list of fields
    else:
        date_fields = []

    result = describe_csv(input_tbl, date_fields)
    print("SCHEMA INFO")
    print(result["schema"])
    print("DATA CHARACTERISTICS OF NUMERIC FIELDS")
    print(result["characteristics"])
    print("UNIQUENESS OF FIELDS")
    print(result["uniqueness"])

if __name__ == '__main__':
    main()
