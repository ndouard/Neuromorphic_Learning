"""
Authors: Nicolas Douard & Anthony Beninati

Note that files should be placed in the training and testing folders. 
Each class should have a unique name. 
This script will use all files in the training and testing folders to build trainlist.
Trainlist text file is a list of relative paths and class ids separated by a space where class id is an incremented integer.

User specifies path to training and testing folders "files_path".
Script gets list of folders in that folder (classes).
Script will, for each class, lists path which is classname/filename and increment class id starting with 1.
"""

from os import listdir, walk, system
from os.path import isfile, join
from enum import Enum
import logging
import time
import os

class List(Enum):
    TRAIN = 1
    TEST  = 2

def register_pause_before_closing_console():
    import atexit
    if os.name == 'nt':
        from win32api import GetConsoleTitle
        if not GetConsoleTitle().startswith(os.environ['COMSPEC']):
            atexit.register(lambda: os.system('pause'))

def add_to_list_test(curr_file: str, f, len_to_discard: int):
    f.write(curr_file[len_to_discard:] + '\n')  # python will convert \n to os.linesep
    
def add_to_list_train(curr_file: str, id: int, f, len_to_discard: int):
    f.write(curr_file[len_to_discard:] + ' ' + id + '\n')  # python will convert \n to os.linesep
    
def create_list(list_name: str, files_path: str, list_type: int):
    with open(list_name, 'w') as new_list:
        len_to_discard = len(files_path) + 1

        folders = [x[0] for x in walk(files_path)]
        print(folders)

        # drop current dir
        folders.pop(0)

        curr_id = 1 # init id at 1
        for k in range(len(folders)):
            only_files = [f for f in listdir(folders[k]) if isfile(join(folders[k], f))]
            for l in range(len(only_files)):
                curr_file = folders[k] + '/' + only_files[l]
                print('Current File: ' + curr_file)
                
                # Write appropriate line to file depending on list type
                if list_type == List.TRAIN:
                    add_to_list_train(curr_file, str(curr_id), new_list, len_to_discard)
                elif list_type == List.TEST:
                    add_to_list_test(curr_file, new_list, len_to_discard)
                else:
                    raise SystemExit('Error: Invalid list type provided to create_list')
            curr_id += 1

create_list('trainlist01.txt', './train', List.TRAIN)
create_list('testlist01.txt', './test', List.TEST)


if __name__ == '__main__':
	register_pause_before_closing_console()

