#
"""
finder.py: combine what we learned from find files and import manager.
"""
 
import sqlite3;
import os;
import sys; 
from find_file import *;
from tuple_comparisons import *;
from import_manager import *; # might upgrade the import manager to use an object... that would make inheritance nicer.

# why were there a bunch of arbitrary spaces?
# I could use compare files to see what's working.
#
# I'm not sure what all needs to be added into this module.

# I think that this might not be directly necessary to inherit safe_management.
class find_manager: #(import_manager.safe_management):
    """
    """
    # use the db_filename variable to determine which database to use - not threadsafe.
    pass;
    
    # now we're using a 
    def __init__(self, dbname = None):
        self.db_filename = import_manager.import_management.db_filename;
        # I need to make a thread safe clone of this module.
        pass;
    # lets
    
    def find_most_recent_file_where_not_in_x(path,pattern = ""):
        """:::
        what in the world is wrong with me for naming this thing - 
        anyway I'll supply some syntactic sugar to make it easier to use.
        :::"""
        pass;
        # I'm honestly not sure how I'm going to implement this...