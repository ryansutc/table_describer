from table_describer import tbl_desc as td
import os


def test_sample():
    # Check that tool runs on sample data
    sampletable = r".\data\sampleTable.csv"
    td.describe_csv(__get_file_path(sampletable), ["creationdate"])


def __get_file_path(relpath):
    '''
    workaround so that TravisCI can discover the files
    :param relpath: path to file relative to this file
    :return: full path to file
    '''

    root_folder = os.path.join(os.path.dirname(__file__))
    full_file_path = os.path.join(root_folder, relpath)
    print(full_file_path)
    return full_file_path