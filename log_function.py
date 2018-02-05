
import datetime

def log_output(contents, logname = "activity_log.log"):
    """
    consistently write the files output to a log.
    """
    n = datetime.datetime.now # get the time the value appears
    with open(logname,'a') as log:
        if type(contents) == list:
            for a in contents:
                log.write("%s\t%s"%(n().strftime("%Y-%m-%d %H:%M"),str(a)));
                if "\n" not in a:
                    log.write("\n");
        else:
            log.write("%s\t%s"%(n().strftime("%Y-%m-%d %H:%M"),str(contents)))
            if "\n" not in contents:
                log.write("\n");
