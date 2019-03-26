#
"""
finder.py: combine what we learned from find files and import manager.
Might set up a debug variant of these modules.
"""
 
import sqlite3;
import os;
import sys; 
from find_file import *;
from tuple_comparisons import *;
#
sys.path.append(".");
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
        #self.db_filename = import_manager.import_management.db_filename;
        # I need to make a thread safe clone of this module.
        self.selection_manager = safe_management();
        pass;
    # lets
    
    def find_most_recent_file_where_not_in_x(self,path,pattern = ""):
        """:::
        what in the world is wrong with me for naming this thing - 
        anyway I'll supply some syntactic sugar to make it easier to use.
        somehthing between the original and this version is causing the issue.
        it's odd that ...
        :::"""
        pass
        # minimalist approach. if they pass the wrong stuff, let it ride.
        path_items = []
        for a in os.listdir(path):
            try:
                if os.path.isabs(path):
                    a = search_path+os.sep+a;
                local_item = [];
                if pattern not in a: continue;
                local_item.append(a); local_item.append(os.path.getmtime(a));
                path_items.append(tuple(local_item))
            except Exception as E:
                print(E);
        remove_paths = []
        for a in path_items:
            try:
                if self.selection_manager.has_file(a)>0:
                    #print("This has been imported!");
                    remove_paths.append(a);
            except Exception as EE: print(EE);
        for a in remove_paths:
            path_items.remove(a);
            #print("removed %s from search."%(a));
        most_recent = max_tup(path_items,1);
        print(most_recent);
        input();
        self.selection_manager.add_file(most_recent);
        return most_recent; # I'm going to change this up to keepgoing to the file date.