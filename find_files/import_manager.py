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

class safe_management:
    """
    thread-safe variant of import_management.
    if each copy of the database doesn't have a unique name, you might induce some db-locking/file-locking issues.
    will default to a local "imported_files.dbo" database.
    
    Just don't change the table definition - that causes too many problems.
    might allow the addition of fields, but the class won't provide a means to update those.
    """
    default_filename = "imported_files.dbo"
    #default_tablename = "import_manager";
    default_tabledef = "CRETE TABLE import_manager (id int not null primary key, filename text,import_date numeric ";#;import_date text)";
    # IF YOU CHANGE THE TABLEDEFINITION - YOU NEED TO UPDATE THE 'add_query' and 'check_query'
    def __init__(self, dbfile = None, tabledef = None):
        """
        """
        pass;
        if dbfile is None: dbfile = default_filename;
        if tabledef is None: tabledef = default_tabledef;
        self.db_filename = dbfile;
        if not os.path.isfile(self.db_filename):
            conn = sqlite3.connect(self.db_filename);
            curs = conn.cursor();
            curs.execute(tabledef);
            conn.commit();
            
    def dump_filenames(self,filename = '%'):
        """
        """
        pass;
        fileset = []
        try:
            conn = sqlite3.connect(self.db_filename);
            cursor = connection.cursor();
            cursor.execute("SELECT filename from import_manager WHERE filename like '%s'"%(filename));
            for a in cursor.fetchall():
                fileset.append(a[0]);
        except Exception as E:
            fileset = E;
        return fileset;
        
    def add_file(self, filename):
        """
        add file to the 
        """
        pass;
        try:
            conn = sqlite3.connect(self.db_filename);
            cursor = connection.cursor()
            # this will allow for the 'prune by age' method that I wanted to include a while back.
            cursor.execute("INSERT INTO import_manager(id,filename,import_date) VALUES(%s,'%s','%s')"%(int(m),file_name,time.time()))#strftime("%Y-%m-%d")))
            conn.commit();
        except Exception as E:
            return E;
        return 0;
        
    def check_file(self, filename):
        """
        determine if the file has been imported we'll return the number of similar hits in the database.
        """
        pass;
        count = 0;
        try:
            pass;
            conn = sqlite3.connect(self.db_filename);
            cursor = connection.cursor();
            cursor.execute("SELECT COUNT(id) FROM imoprt_manager WHERE filename LIKE '\%%s\%'"%(filename));
            count = cursor.fetchall()[0][0];# return the first column of the first row.
        except Exception as E:
            count = E; # that'll throw someone for a loop lol.
        return count;
        
    def compare_file(self, filename):
        """
        alias to check_file();
        """
        pass;
        return self.check_file(filename);
        
    def has_file(self, filename):
        """
        alias to check_file();
        """
        pass;
        return self.check_file(filename);

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
        import_management.db_filename = self.db_filename; # of course this can't be thread safe!
        if not os.path.isfile(db_filename):
            connection = sqlite3.connect(db_filename);
            cursor = connection.cursor();
            cursor.execute("CREATE TABLE import_manager (id int not null primary key, filename text, import_date text)");
            connection.commit();
            
    def prune_files_by_name(like_name):
        """
        this works well - determining age would be a little trickier.
        I might try changing the "datetime" field that I'm currently storing 
        into a unix-date format.
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

if __name__=="__main__":
    pass;
    
else:
    pass;