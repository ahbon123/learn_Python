# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:39:08 2019

@author: ZHAO
"""

#https://stackoverflow.com/questions/23488924/how-to-delete-recursively-empty-folders-in-python3

import os

path = 'F:/'

def remove_empty_dir(path):
    try:
        os.rmdir(path)
    except OSError:
        pass

def remove_empty_dirs(path):
    for root, dirnames, filenames in os.walk(path, topdown=False):
        for dirname in dirnames:
            remove_empty_dir(os.path.realpath(os.path.join(root, dirname)))

remove_empty_dirs(path)
