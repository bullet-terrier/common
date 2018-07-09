# Common

set of common functions that find their way into my code frequently.

Working on porting the code to work on older versions of python as 
well as it does on python 3.x

Currently looks like the files are now backwards compatible, so I'll
continue to modify them as more errors are encountered.

# filestats.py
mechanism to display and calculate the age/last access time of files.
essentially syntactical sugar over os.path.

# kwargv.py
mechanism for handling keyword based arguments in a consistent and
repeatable manner - is a repeated dependency in many of the modules
released by bullet-terrier.

# 2018-07-09
added module - filestats.py - get size/time/date in a printable/calculatable format.
