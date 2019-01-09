#!/usr/bin/env python
import os
import shutil

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


if __name__ == '__main__':
    shutil.make_archive(__get_file_path("tbl_desc"), "zip",
                            __get_file_path("dist/"))
    print("zipping file...")
    print("done")
