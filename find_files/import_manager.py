#
"""
Expose some calls to simplify the procedure to prevent duplicate selection.
adding in some support to prevent the reimportation of files.
this unit needs to be self contained.

I'll need some accessor methods to allow querying the results.
local settings should detrmine the pathing, but I'll try to reduce
complexity as much as humanly possible.

this is the local copy of the import_manager script - I'm going to expand it to be object oriented.
"""

import sys;
import sqlite3;
import os;
import time;

# note - the main thing to note is that the ./imported_files.dbo will be used across all of the outputs.

# regardless of whether or not executing as main, we'll create the database in the local directory.
# *MIGHT* encounter issues with the 

class import_management:
    """
    NOTE! most of the functions defined here will be targeting the "import_management" class, not an instance of the class.
    
    """
    db_filename = None;
    def __init__(self, filename_override = None):
        """
        let's work on an initialization file - I'm going to change some of these to work on the OS module.
        """
        db_filename = "%s%simported_files.dbo"%(os.curdir,os.sep);#+"imported_files.dbo"; # they'll need to go way out of the way in order to adjust this.
        if filename_override is not None: db_filename = filename_override;
        self.db_filename = db_filename;
        if not os.path.isfile(db_filename):
            connection = sqlite3.connect(db_filename);
            cursor = connection.cursor();
            cursor.execute("CREATE TABLE import_manager (id int not null primary key, filename text, import_date text)");
            connection.commit();
            
    def prune_files_by_name(like_name):
        """
        """
        pass;
        deleted_num = 0;
        connection = sqlite3.connect(db_filename);
        cursor = connection.cursor();
        cursor.execute("SELECT COUNT(filename) FROM import_manager WHERE filename LIKE '%s'"%(like_name));
        deleted_num = cursor.fetchall()[0][0]; # first row, first column of the count.
        cursor.execute("DELETE FROM import_manager WHERE filename LIKE '%s'"%(like_name))
        connection.commit();
        return deleted_num;            
        
    def prune_old_files(older_than):
        """
        """
        pass;
        
    # now to load up the next series of methods.
    def add_file(file_name):
        """
        only will read/write from ./imported_files.dbo;
        """
        pass;
        connection = sqlite3.connect("./imported_files.dbo");
        cursor = connection.cursor();
        cursor.execute("SELECT MAX(id) FROM import_manager");
        m = cursor.fetchall()[0][0]; # should be the first item of the first row.
        if m is None: m = 1;
        else: m +=1
        cursor.execute("INSERT INTO import_manager(id,filename,import_date) VALUES(%s,'%s','%s')"%(int(m),file_name,time.strftime("%Y-%m-%d")))
        connection.commit();
        #print("added %s"%(a))
        return;
        
    def compare_file(file_name):
        """
        return boolean - file exists or not.
        """
        pass;
        connection = sqlite3.connect("./imported_files.dbo");
        cursor = connection.cursor();
        retval = False;
        m = cursor.execute("SELECT filename FROM import_manager").fetchall()
        if file_name in m: # need to make sure that this works.
            retval = True;
        for a in m: 
            print(a[0]);
            if file_name == a[0]: retval = True;
        return retval;
