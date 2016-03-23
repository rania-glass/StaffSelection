import os
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
from Messages import PrintMessages
from Modules import handleCSV
from Modules import Sorter
from Modules import SortFileByName



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
        docCategory = str(input("Enter the category of these documents in quotes. (eg ''Recommendations'', ''Applications'', etc)"))
        Sorter.sortApps(inFile, docCategory)

    else:
        print "Try again with a .txt or a .csv file."
        getFile()


def sortFiles():
    print "Please select the CSV file that contains the list of names to be sorted away."
    inFile = askopenfilename();
    print "Please enter the name of the folder you would like the names on that CSV to be sorted into, surrounded by quotes."
    newDirName = input("Such as, ''Hired'' or ''Archived''")
    SortFileByName.sortIntoDir(inFile, newDirName)
    print "The files were sorted accordingly."


on = True;
while on:
    print "\n"
    print "1: Generate files from existing TXT or CSV."
    print "2: Sort existing files into the proper folders by name"
    print "3: Sort files according to a new and separate list"
    print "4: Quit"
    option = input("Enter your selection here:")

    if option == 4:
        on = False
    elif option == 1:
        getFile()
    elif option == 2:
        print "Please select the directory you would like sorted."
        path = askdirectory()
        path = os.path.abspath(path)
        print "inDir: ", path
        SortFileByName.sort(path)

    elif option == 3:
        print "Please select the CSV containing the list of names to be moved into another folder."
        inDir = askopenfilename()

        newDirName = input("Please enter the name of the new folder into which the files will be sorted.")
        SortFileByName.sortIntoDir(inDir, newDirName)
    else:
        print "\n That is not a valid input. Please try again. \n"

    print "Thanks for using Student Staff Selection Automation!"
