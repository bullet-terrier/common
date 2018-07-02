#
"""
Building up a "base pump" class;

This will need to be separated from the PWOP task,
as it should become its own module.
"""

# bringing in kwargv since I'll use it for the initializer.
# might have an easier time reimplementing kwargv.reconcile in this mechanism.
import kwargv


class table:
    """
    defining a table class- should be close to
    what the insured and policy tables looked like.
    
    I'm going to set up a bunch of placeholder methods.
    """
    # Use an array of tuples to store the field name and the value
    # use strings to contain this information so it can be emitted as SQL.
    # I guess an empty fields initializeer is okay.
    # standard field ('table_id','int'),('table_name','varchar(x)') etc.
    # I've set this to be the main unit rather than calling the "get_fields" from keys.
    fields = []
    
    name = None
    
    # Just a note - might want to look at making a case-insensitive version later.
    keys = {
      "name":None,
      "fields":None,
      "database":None,
      "server":None,
      "user":None,
      "password":None, # probably shouldn't use this - but I'll include it for now.
      "":None
    }    
    
    def get_insert_statement(self):
        """
        Generate a generic insert statement based on object fields.
        
        Be sure that the insert statement has the correct number of values in the
        format string etc. It could cause issues if it doesn't.
        """
        pass
        if len(self.fields) == 0:
            self.fields = self.get_fields()
        self.insert_statement = "INSERT INTO %s ("%(self.keys['name'])
        for a in self.fields:
            self.insert_statement +="\n%s"%(a[0]); # pull the field name.
            if len(self.fields)-1 != self.fields.index(a): self.insert_statement+=',';
        self.insert_statement += ") VALUES ("
        for a in range(0,len(self.fields)):
            if 'char' in self.fields[a][1].lower(): self.insert_statement+="'%s'"
            elif 'date' in self.fields[a][1].lower(): self.insert_statement+="'%s'"
            else: self.insert_statement+="%s"
            if a+1 < len(self.fields): self.insert_statement+=","
        self.insert_statement+=")";
        return self.insert_statement;
        
    def get_create_statement(self):
        """
        """
        pass
        self.create_statement = "CREATE TABLE %s ("%(self.keys['name'])
        if len(self.fields) == 0:
            self.fields = self.get_fields();
        for a in self.fields:
            self.create_statement+="\n%s %s"%(a[0],a[1]);
            if len(self.fields)-1 > self.fields.index(a): self.create_statement+=",";
        self.create_statement+=")";
        return self.create_statement;
        
    def get_fields(self):
        """
        Extract the fields into an easier to read format.
        Only execute get_fields once, and either store 
        the output, or reference self.fields.
        """
        pass;
        print("Just a warning: access self.fields from now on - since the keys are not thread safe.")
        self.fields = [];
        for a in self.keys['fields']:
            self.fields.append(a);
        return self.fields;
        
    def establish_connection(self):
        """
        todo: implement this functionality.
        """
        raise Exception("Not Implemented");
        
    def get_select(self,fields=None):
        """
        todo: implement this functionality.
        """
        raise Exception("Not Implemented");
        
    def __init__(self,**kwargs):
        """
        Need to identify what needs to go into the constructor- honestly there isn't too much
        that needs to be done right off the cuff.
        """
        pass
        # use the keywords to instantiate the object.
        self.keys = kwargv.reconcile(table.keys,kwargs);
        self.fields = self.get_fields();
        self.name = self.keys['name']
        # note: self.keys will override the base class (not sure why)