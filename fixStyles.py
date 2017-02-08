#Edit code so that the stylesheets load correctly on github pages
#Ross Andrewartha

#Import modules
import sys, time, os, fileinput
from fnmatch import fnmatch

#Constants
root = 'F:\Ross\Documents\GitHub\W-R-A.github.io'
pattern = "*.html"

#Define function to end program
def quitProg():
    q = input('Press any key to exit')
    sys.exit()

#Define function to replace refrences
def replace(file):
    with fileinput.input(file,inplace=True) as f:
        for line in f:
            line = line.replace("_frontend", "frontend")
            line = line.replace("?ver=0.0.14", "")
            line = line.replace("?ver=4.7.2", "")
            print(line, end='')
    print("Replaced references in ", file)

#List all html files in folder and subfolders        
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            #Replace references in file
            replace(os.path.join(path, name))

#Exit
quitProg()
