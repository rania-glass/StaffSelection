import re
import os


def sortApps(inFile, docCategory):

    theFile = file(inFile, "r")
    data = theFile.read()
    theFile.close()

    #retrieve the directory that the input file is stored in
    directoryPath = os.path.dirname(inFile)

    #declare a new subdir within that directory
    directory = directoryPath + "/Files_Created"

    #check to see if that subdir already exists, if not,
    #create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Split data on GTID
    applicationArray = re.split("90[0-9]{7}\s", data)
    # Remove the blank thing at the front (from splitting)
    applicationArray.pop(0)
    print "Found " + str(len(applicationArray)) + " applications."
    GTIDArray = re.findall("90[0-9]{7}\s", data)
    print "Found " + str(len(GTIDArray)) + " GTID's."
    #if not the same length, throw a custom exception

    # GTIDARray and application array should have identical lengths
    if not os.path.exists(directory):
        os.makedirs(directory)
    # For each file, read in the first & last names, create filename
    # and write the entire application to that file
    for GTID, application in zip(GTIDArray, applicationArray):
        # Create files directory
        # directory = "Applications"
        # if not os.path.exists(directory):
        #     os.makedirs(directory)

        toWrite = GTID + "\n" + application

        s = re.search(r"((90[0-9]{7})(\s*\n*\s*)(([A-Z][a-z]*[^\S\r\n]*)*\n*[^\S\r\n]*)(([A-Z][a-z]*[^\S\r\n]*)*)*)", toWrite)

        untrimmed = ''.join([i for i in s.group() if not i.isdigit()])
        trimmed1 = untrimmed.strip()
        trimmed2 = trimmed1.replace("\n", ", ")
        candidateName = trimmed2.replace(", ,",", ")

        print "Candidate Name: " + str(candidateName)
        dirName = directory + "/" + candidateName
        filename = directory + "/" + candidateName + "/" + candidateName + " - " + str(docCategory) + ".doc"
        if not os.path.exists(dirName):
            os.makedirs(dirName)

        # Create the file, writing the GTID and then the application content
        # We have the write the GTID because it was rmemoved on the split.
        newFile = file(filename, "w")
        newFile.write(toWrite)
        newFile.close()
