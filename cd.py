import os
import sys;


def cd(path=None):
    """
    """
    if path is None: path = os.curdir;
    else: 
        try: os.chdir(path);
        except Exception as EC:
            print(str(EC)+"ERROR...")
            cd(path=None);
    for a in os.listdir(os.curdir):
        print(a);
        
if __name__=="__main__":
    for a in sys.argv[1:]:
        cd(a);
    if len(sys.argv)<=1: cd();