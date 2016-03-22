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
        print "What would you like to do with this file?"
        print "Press the key that corresponds to what you want to do."
        print "1: Separate each row into its own document"
        print "2: Merge all of the data into a text document"
        selection = input("Enter your selection, then press 'Enter' ")
        docCategory = input("Enter the category of tese documents in quotes. (eg ''Recommendations'', ''Applications'', etc)")
        docCategory = str(docCategory)
        if selection == 1:
            handleCSV.separate(inFile, docCategory)
        elif selection == 2:
            handleCSV.merge(inFile)
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
