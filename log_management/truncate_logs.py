#
"""
Abbreviated Log-Purging script.
Making it minimalist for some of our more embedded pieces of software.
"""

import sys;
import os;
import time;

scan_path = "";
file_pattern = ".log";
file_age = (7*24)*(60)*(60)

killed_recently = []
exceptions = []
# foreach file in the scan_path, check for file_pattern

if not os.isdir(scan_path): raise Exception("Invalid Argument, scan_path must be a valid directory")

for _file_ in os.listdir(scan_path):
    try:
        if file_pattern in _file_ and os.path.getctime(_file_) > file_age:
            os.remove(_file_);
            killed_recently.append(_file_);
    except Exception as E:
        exceptions.append(E);
        print(str(E));
        
with open("./truncate_logs.log",'w') as lgs:
    for a in exceptions: lgs.write(time.strftime("%Y-%m-%d %H:%M")+"\t"+str(a)+"\r\n");
    for b in killed_recently: lgs.write(time.strftime("%Y-%m-%d %H:%M")+"\t"+b+"\r\n");
