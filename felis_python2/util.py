import os, shutil
import subprocess

def copy(path):
    """

    :param path:
    :return:
    """
    # build lecture dir
    new_dir = os.path.join(path, 'lectures')
    lecture_dir = os.path.join(os.path.dirname(__file__), 'lectures')

    # check the path
    if not os.path.isdir(path):
        raise TypeError('%s is not a directory')

    shutil.copytree(lecture_dir, new_dir)


def run():
    """

    :return:
    """
    try:
        os.chdir(os.path.join(os.path.dirname(__file__), 'lectures'))
        subprocess.run(['jupyter', 'notebook'])
    except KeyboardInterrupt:
        print('Jupter interrupted by User input...')