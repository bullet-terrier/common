#
"""
py_benchmark


run programs passed in the argv which will
be the main source of information.

steps:

1) initialize this module
2) validate the path passed in
3) run the program at path and return time taken to complete.
4) that's it.


This is a generalized process that will function on non-python 
processes as well.
"""

import time;
import sys;
import subprocess;
import os;
import kwargv; # I forgot that I'll need a mechanism to pass parameters.
import math;

def help():
    print("""
===============================================================================
py_benchmark.py
    
ENTER THE PROCESS TO CALL WITH "process <process_name>" and 
pass arguments with "args ["]<arguments to program>["]"
round the seconds with "round True";
round the minutes with "minutes True";
round the hours with "hours True";
round the days with "days True"

all of the options can be passed in any order

ex:
  py_benchmark.py process py_benchmark.py hours 1 arg "process py_benchmark.py"

Not passing process, or passing "help" will display this message.

===============================================================================
    """
    )
    quit();


def main(args):
    """
    """
    s_time = None;
    e_time = None;
    d_time = None;
    b_delt = None
    t_times = []
    scale = 'second(s)'
    dct = {
      "process":None,
      "args":None,
      "round":None,
      "minutes":None,
      "hours":None,
      "help":None,
      "days":None
      }      
    dct = kwargv.reconcile(dct,args);   
    if dct['process'] is None: 
        help();
    elif dct['help'] is not None: 
        help();   
    # this portion shouldn't be accessible for now.
    if type(dct["process"])==list:
        for a in dct["process"]:
            if not os.path.isfile(a): continue;
            s_time = time.time();
            subprocess.call(a)
            e_time = time.time();
            d_time = e_time-s_time;
            t_times.append((s_time,e_time,d_time));
    else:
        s_time = time.time();
        subprocess.call(dct["process"],dct["args"]);
        e_time = time.time();
        b_delt = e_time-s_time;
        d_time = e_time-s_time;
        if dct['minutes']: 
            d_time = math.ceil(b_delt)/60;
            scale='minute(s)'
            #print("Time in minutes: %s"%(d_time));
        if dct['hours']:
            d_time = math.ceil(b_delt)/360;
            scale = 'hour(s)'
            #print("Time in hour(s): %s"%(d_time));
        if dct['days']:
            d_time = math.ceil(b_delt)/8640;
            scale = 'day(s)'
            #print("Time in day(s): %s"%(d_time));
        if dct['round']: d_time = math.ceil(d_time);
        t_times.append(scale);
        t_times.append((s_time,e_time,d_time));
    return t_times;

if __name__=="__main__":
    print("very good.");
    print("Time is: %s"%(time.strftime("%H:%M:%S")));
    if len(sys.argv) < 3:
        help();    
    times = main(kwargv.arg2kwarg(sys.argv));
    sys.stdout.write("Time to complete was %s %s.. \n"%(times[-1][2],times[0]));
    sys.stdout.write("Time now is: %s"%(time.strftime("%H:%M:%S")));
else:
    raise Exception("This module not intended for import");
    
