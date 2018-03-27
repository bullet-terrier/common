#!C:/Python34/python.exe
"""
This is ready for integration into the "COMMON"
library. 

...


"""

# testing kwargs on __name__=="__main__";

import sys;
import time;

n = time.time();

# could use information
kywds = {
    "-v":None # I should add a mechanism that will help set up "flags";
    ,"-o":None # write output to this directory.... Could add mechanism to pipe info through stdin/out
}


def reconcile(dict_1, dict_2):
    """
    update dict_1 withe the contents of dict_2;
    """
    pass
    for a in dict_2.keys():
        dict_1.update({a:dict_2[a]});
    del dict_2;
    return dict_1;


def arg2kwarg(lst):
    """
    prettyy much on a whim, I'm building a tool
    to allow keyword arguments to be pulled in from
    sys.argv.
    
    The nature of this function *should* allow it to 
    work with the raw value for sys.argv.
    
    NOTE: will trash first arg if list is not even.
          this means that we'll be dealing with some
          quirks brought on by the technical decisions made.
    """
    pass
    if len(lst)%2==1:
        # well, we know now that we're working with 
        # an odd list. handle it...
        pass;
        # this means that we don't have a set of key value pairs...
        # each key should have one associated argument of indeterminate type...
        # SOLUTION: throw away first position.
        lst = lst[1:];
    elif len(lst)%2==0:
        # well, we know now that we're working with
        # an even list. do something
        # nothing to do here really. Could recursively force the list to even...
        pass;
    kwargs ={};    
    while len(lst)>0:
        if len(lst)%2==1:
            ky = lst.pop()
            kwargs.update({ky:vl})
            ky,vl = None,None;
        else:
            vl = lst.pop()
    return kwargs;
    
def reconcile(dict_1, dict_2):
    """
    update dict_1 withe the contents of dict_2;
    """
    pass
    for a in dict_2.keys():
        dict_1.update({a:dict_2[a]});
    del dict_2;
    return dict_1;

def main_test(sargs):
    sys.stdout.write("Args in: ")
    for a in sargs:
        sys.stdout.write(a+" ");
    sys.stdout.write("\n");
    dct = arg2kwarg(sargs);
    sys.stdout.write("key:value pairs: \n")
    for a in dct.keys():
        sys.stdout.write("%s:%s\n"%(str(a),str(dct[a])))
    return;        

#if __name__!="__main__": raise Exception("yOou MuUst rUN ThiS aS mAIn!!");
#else:
#    print("working");
    
#main_test(sys.argv);
#print(time.time()-n)