import os
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
from Messages import PrintMessages
from Modules import handleCSV



def getFile():
    #get the file to be operated on
    print "Please select a .txt or a .csv file to be operated on."
    inFile = askopenfilename();

    print "You have selected " + os.path.basename(inFile) + " to be operated on."
    ext = os.path.splitext(inFile)[1]
    print "The output of the operation(s) will be stored in the same directory as the file "
    print "that you have selected."

    if ext == ".csv":
        print "This file can be separated by row into multiple documents. To do that, press '1'."
        selection = input()
        docCategory = input("Enter the category of these documents in quotes. (eg ''Recommendations'', ''Applications'', etc)")
        docCategory = str(docCategory)
        if selection == 1:
            handleCSV.separate(inFile, docCategory)
        else:
            print "That is not an option. Let's start over."
            getFile()

    elif ext == ".txt":
        print "This file can be separated by GTID. Press '1' to perform this operation."
        selection = input()
        handleTXT(selection, inFile)

    else:
        print "Try again with a .txt or a .csv file."
        getFile()


getFile()
