#
"""
finder.py: combine what we learned from find files and import manager.
"""
 
import sqlite3;
import os;
import sys; 
from find_file import *;
from import_manager import *; # might upgrade the import manager to use an object... that would make inheritance nicer.

# why were there a bunch of arbitrary spaces?
# I could use compare files to see what's working.
