import os
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
from Messages import PrintMessages



def getFile():
    #get the file to be operated on
    print "Please select a file to be operated on"

    inFile = askopenfilename();


    print "You have selected " + os.path.basename(inFile) + " to be operated on."
    ext = os.path.splitext(inFile)[1]
    print ext
    if ext == ".csv":
        print "csv options"
    elif ext == ".txt":
        print "txt options"
    else:
        print "Try again with a .txt or a .csv file."
        getFile()


getFile()
