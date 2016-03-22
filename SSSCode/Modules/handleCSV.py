import os
import re
import csv

#file must be a CSV file
#user selected one of the options from the menu on the last interaction
#this file handles the options selected on the previous menu
#the options were to separate by row
#or merge into one document


#separate a CSV into several documents, named for their second field
#name the documents according to what they are and who they belong to
#param filename is the file to parse data from
#docCategory is the user-specified document category that will become part of
#the file name
#output is saved to a new subdir of the directory that the input file is saved in
def separate(filename, docCategory):

    #retrieve the directory that the input file is stored in
    directoryPath = os.path.dirname(filename)

    #declare a new subdir within that directory
    directory = directoryPath + "/Files_Created"

    #check to see if that subdir already exists, if not,
    #create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    #using Python CSV lib
    #read the CSV file content, separately from the header
    with open(filename, "r") as fileToSplit:
        reader = csv.reader(fileToSplit)
        headers = reader.next()

        #for each row of content, create a file named after its second column
    #to change the column that the file is named after, change the '1' in "row[1]"
    #the indices of the rows start at 0, so 0 is the first, and 1 is the second cell
        for row in reader:
            fileName = directory + "/" + row[1] + " - " + str(docCategory) + ".doc"
            if not os.path.exists(fileName):
                newFile = file(fileName, "w")

                #give user confirmation that something is happening
                print "Writing data to", os.path.basename(fileName)

                #for each cell in each row, write that data with matching header to the document
                for item in range(len(row)):
                    newFile.write("\n" + headers[item] + "\n" + str(row[item]) + "\n")
                newFile.close()
            else:
                fileName = directory + "/" + row[1] + " - " + str(docCategory) + "2.doc"
                newFile = file(fileName, "w")

                #give user confirmation that something is happening
                print "Writing data to", os.path.basename(fileName)

                #for each cell in each row, write that data with matching header to the document
                for item in range(len(row)):
                    newFile.write("\n" + headers[item] + "\n" + str(row[item]) + "\n")
                newFile.close()
