import os
import re
import csv
import shutil

currentpath = os.path.realpath(__file__)
directorypath = re.split(r"(.*)\\Modules\\CreateFolders.py", currentpath)
directorypath = directorypath[1]
print directorypath
#param masterList is the CSV file that contains the candidates names
def createFolders():
    #write to the output directory
    directory = directorypath + "\Staff Selection Output"
    if not os.path.exists(directory + "\Male"):
        os.makedirs(directory + "\Male")
    if not os.path.exists(directory + "\Female"):
        os.makedirs(directory + "\Female")

def CreateCandidateFolders(masterList):
    print masterList
