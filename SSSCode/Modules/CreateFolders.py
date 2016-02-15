import os
import re
import csv
import shutil

currentpath = os.path.realpath(__file__)
directorypath = re.split(r"(.*)\\SSSCode\\Modules\\CreateFolders.py", currentpath)
directorypath = directorypath[1]
print directorypath
#param masterList is the CSV file that contains the candidates names
def createFolders():
    #write to the output directory
    directory = directorypath + "\\SSSCodeTestingMaterial\StaffSelectionOutput"
    print "dir", directory
    if not os.path.exists(directory + "\Male"):
        print "no male directory exists"
        os.makedirs(directory + "\Male")
    if not os.path.exists(directory + "\Female"):
        os.makedirs(directory + "\Female")

def CreateCandidateFolders(masterList):
    print masterList
