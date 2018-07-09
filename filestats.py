#
"""
using stdlib functions to determine information about a file.
we'll assume that we're working with a file, so I'm not going
to add any extra checks in here.
"""

import time;
from os import path;

def get_size(file):
    "lumping this in since it's related to path..."
    if path.isfile(file):
        return path.getsize(file); 

def get_age(file):
    "get time since file creation (in seconds)"
    if path.isfile(file):
        return time.time()-path.getctime(file);  

def get_last_access(file):
    "get time since last file-access (in seconds)"
    if path.isfile(file):
        return time.time()-path.getatime(file);

def get_last_modification(file):
    "get time since last file modification (in seconds)"
    if path.isfile(file):
        return time.time()-path.getmtime(file);

def printable_creation(file):
    if path.isfile(file):
        return time.ctime(path.getctime(file));

def printable_access(file):
    if path.isfile(file):
        return time.ctime(path.getatime(file));

def printable_modification(file):
    if path.isfile(file):
        return time.ctime(path.getmtime(file));

if __name__!="__main__":
    #with open('filestats.py','r') as fs:
    fs = ["get_size(file)","get_age(file)","get_last_access(file)","get_last_modification(file)"
    ,"printable_creation(file)","printable_access(file)","printable_modification(file)"
    ]
    for a in fs:
        if "def" in a: print(a+"\n");
