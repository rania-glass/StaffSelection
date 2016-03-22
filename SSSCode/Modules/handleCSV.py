import os
import re
import csv

#file must be a CSV file
#user selected one of the options from the menu on the last interaction
#this file handles the options selected on the previous menu
#the options were to separate by row
#or merge into one document
#returns the output

#the output will be saved to an output folder
def separate(filename, docCategory):

    print "Calling handleCSV..."
    directoryPath = os.path.dirname(filename)
    directory = directoryPath + "/Files_Created"

    if not os.path.exists(directory):
        os.makedirs(directory)

    #separate each row into its own document
    with open(filename, "r") as fileToSplit:
        reader = csv.reader(fileToSplit)
        headers = reader.next()




        for row in reader:
            fileName = directory + "/" + row[1] + " - " + str(docCategory) + ".txt"
            print os.path.basename(fileName)
            newFile = file(fileName, "w")
            for item in range(len(row)):
                newFile.write("\n" + headers[item] + "\n" + str(row[item]) + "\n")
            newFile.close()



def merge(filename):
    return 0
