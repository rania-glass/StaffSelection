import os
import csv
import shutil

#([A-Z][a-z]*)+(.*)([A-Z][a-z]*)+


def sort(path):
    print "PATH: ", path
    allfolders = []
    allfiles = []

    for node in os.walk(path):
        (dirpath, dirs, files) = node
        folders = (dirs)
        allfolders.append(dirs)
        allfiles.append(files)

    filestosort = allfiles[0]
    directory = allfolders[0]

    print filestosort
    print directory

    for doc in filestosort:
        for folder in directory:
            if folder in doc:
                newpath = path+"\\"+folder+"\\"
                print doc
                print newpath
                shutil.move(doc, newpath)
                #os.rename(path, newpath[1])
                #print doc, " goes in ", folder

def sortIntoDir(inFile, newDirName):

    #get the current working directory
    headDir = os.path.dirname(inFile)

    #create, if necessary, a new subdirectory within that working directory
    #titled according to the user's specification
    newDir = headDir + "/" + str(newDirName)
    if not os.path.exists(newDir):
        os.makedirs(newDir)

    names = []
    allfiles = []
    allfolders = []

    for node in os.walk(headDir):
        (dirpath, dirs, files) = node
        folders = (dirs)
        allfolders.append(dirs)
        allfiles.append(files)

    with open(inFile, "r") as namesToSort:
        reader = csv.reader(namesToSort)

        for row in reader:
            names.append(row[1])


    for folder in directory:
        if str(folder) in names:
            shutil.move(folder, newDir)
            #os.rename(path, newpath[1])
            print doc, " was moved to ", os.path.basename(newDir)
