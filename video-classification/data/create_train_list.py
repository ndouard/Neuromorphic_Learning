"""
Author: Nicolas Douard

Note that files should be placed in the training folder. 
Each class should have a unique name. 
This script will use all files in the training folder to build trainlist.
Trainlist text file is a list of relative paths and class ids separated by a space where class id is an incremented integer.

User specifies path to training folder "files_path".
Script gets list of folders in that folder (classes).
Script will, for each class, lists path which is classname/filename and increment class id starting with 1.
"""

from os import listdir, walk, system
from os.path import isfile, join
import logging
import time
import os

# print to the standard output and append to a log file
# logging.basicConfig(level=logging.INFO, format='%(message)s')
# logger = logging.getLogger()
# logger.addHandler(logging.FileHandler('create_lists.log', 'a'))
# print('*** Starting on ' + time.ctime() + ' ***\n')

def register_pause_before_closing_console():
    import atexit
    if os.name == 'nt':
        from win32api import GetConsoleTitle
        if not GetConsoleTitle().startswith(os.environ['COMSPEC']):
            atexit.register(lambda: os.system('pause'))

f = open('trainlist01.txt', 'w')

def add_to_list(curr_file, id):
    f.write(curr_file[len_to_discard:] + ' ' + id + '\n')  # python will convert \n to os.linesep

files_path = './train' # training path
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
        add_to_list(curr_file, str(curr_id))
    curr_id += 1

f.close()  # you can omit in most cases as the destructor will call it

if __name__ == '__main__':
	register_pause_before_closing_console()

