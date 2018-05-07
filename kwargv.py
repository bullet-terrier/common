#!C:/Python34/python.exe
"""
This is ready for integration into the "COMMON"
library. 

I'm not sure why there are two instances of reconcile - I'm going to need
to look into that.

We'll add a new function args2kwargs (probably too ambiguous)
that will look for "x=y" vs "x x x x x x x x=y x=y" and can 
take additional symbold to look for to split the values.
...

planned changes to the mechanism for parsing lists - looking to using map()
to iterate over longer sets - should allow for faster/better integration
of mini utilities.

v2.0.1
"""

# testing kwargs on __name__=="__main__";

import sys;
import time;

n = time.time();

# could use information
# tweak arg2kwarg to expand and handle some values in list form and others
# that are in dict form...
# or rather add in a new function that wouldn't interfere with the already supported codebase.
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

def args2kwargs_avoid_quotes(lst):
    """
    this should only be called from args2kwargs,
    and only IF there is a chance that the separator
    is contained in a string.
    this will only be called if a flag for args2kwargs
    is set (in args) not (in kwargs)
    
    in this case - for each character in the list - if
    it is within either single or double quotes it will be
    treated as a single argument.
    """
    pass;
    # 

def args2kwargs(lst,*args,**kwargs):
    """
    a wonderful little function that I'm setting up to allow 
    args and kwargs to be passed in.
    I'll probably make as much use of this function as I do
    with the reconcile function that is defined in here as well.

    main premise is to allow sequential/flag type arguments as 
    well as keyword based arguments, which will allow for better
    processing of irregular human input. (need to look at global impact)

    """
    #    main keyword argument is the 'separator' which can have its behavior
    #    modified by passing in "multiple_separators" and passing 
    #    separator=[<separators>]
    pass;
    kgs = {
      "separator":"=" # default splitter is going to be "=" can be overridden.
    }
    kgs = reconcile(kgs,kwargs); # build up the kwarg values.
    r_args = [] # contain   args
    r_krgs = {} # derived r_krls
    r_krls = [] # becomes r_krgs
    # split off the values that only need to be parsed as a list.
    for a in lst:
        # I could make this more robust in order to avoid things contained in
        # strings - however I might fork that off into a separate function.
        if kgs['separator'] in a: r_krls.append(a);
        else: r_args.append(a);
    # we'll use a popping construct here.
    # additionally - we'll know that everything in this contains the 
    # splitter character. If there's a chance that someone is passing 
    # the splitter character within an argument string -then we'll 
    # need to set up some other method of handling that.
    while len(r_krls)>0:
        # I'm going to always treat the left side as the key.
        tmp = r_krls.pop().split(kgs['separator']);
        r_krgs.update({tmp[0]:tmp[1]});
    return r_args,r_krgs;
        
        
    
    


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
