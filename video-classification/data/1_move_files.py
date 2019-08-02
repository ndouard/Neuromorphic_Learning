"""
Run this to move all the files into the appropriate train/test subfolders.

Should only run this file once!
"""

import os
import os.path


def get_class_list(version=''):
    """
    Using one of the train/test files (01, 02, or 03), get the filename
    breakdowns we'll later use to move everything.
    """
    class_filename = os.path.join('lists', 'classInd' + version + '.txt')

    check_class_list(class_filename)

    # Build list of classes

    with open(class_filename) as f:
        class_list = [line.strip().split()[1] for line in list(f)]

    return class_list


def check_class_list(class_filename):
    """
    Ensures that the class file exists and is formatted correctly
    """
    # Ensure that class file exists
    if not os.path.isfile(class_filename):
        print('Error: Class file "' + class_filename + '" does not exist.')
        quit()

    # Ensure that each line in the class file is the proper length
    with open(class_filename, 'r') as f:
        lines = [line.strip().split() for line in list(f)]
        for line in lines:
            if len(line) != 2:
                print('Error: Class file "' + class_filename + '" is formatted incorrectly.')
                quit()


def move_files(class_list: list, group: str):
    """
    This assumes all of our files are currently in train and test directories.
    So move them to the appropriate spot. Only needs to happen once.
    """

    # Test files
    for filename in os.listdir(group):
        # Only process video files
        if not filename.endswith('.avi'):
            continue

        # Determine class
        class_name = ''
        for class_name in class_list:
            if class_name in filename:
                class_name = class_name
                break

        # Class could not be determined
        if class_name == '':
            print('Unknown class for "' + filename + '". Skipping.')

        # Check if this class exists
        if not os.path.exists(os.path.join(group, class_name)):
            print('Creating test folder for ' + class_name)
            os.makedirs(os.path.join(group, class_name))

        # Check if we have already moved this file, or at least that it
        # exists to move.
        if not os.path.exists(os.path.join(group, filename)):
            print("Can't find %s to move. Skipping." % filename)
            continue

        # Move file
        dest = os.path.join(group, class_name, filename)
        print("Moving %s to %s" % (filename, dest))
        os.rename(os.path.join(group, filename), dest)


def main():
    """
    Go through each of our train/test text files and move the videos
    to the right place.
    """
    # Get the videos in groups so we can move them.
    class_list = get_class_list()

    # Move the files.
    move_files(class_list, 'test')
    move_files(class_list, 'train')

    print("Done.")


if __name__ == '__main__':
    main()
