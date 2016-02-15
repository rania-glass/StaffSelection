import csv
import os
import re
import shutil
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() #keep the root window from appearing

#Create the directory containing all the candidate folders
filename = askopenfilename()

with open(filename) as selected:
        reader = csv.reader(selected)
        selectedList = list(reader)

#in the directory chosen by the user in settings
currentpath = os.path.realpath(__file__)
directorypath = re.split(r"(.*)\\SSSCode\\Modules\\ArchiveCandidates.py", currentpath)
searchpath = directorypath[1] + "\\SSSCodeTestingMaterial\\StaffSelectionOutput\\Female"
archivepath = directorypath[1] + "\\SSSCodeTestingMaterial\\StaffSelectionOutput\\Archived"

#generate a list of selected candidates in the format ["last name, first name", ...]
namesList = []
for candidate in range(len(selectedList)):
    namesList.append(searchpath + "\\" + selectedList[candidate][1] + ", " + selectedList[candidate][2])

if not os.path.exists(archivepath):
    os.mkdir(archivepath)

items = []
for root, dirnames, filenames in os.walk(searchpath):
    for dirname in dirnames:
        dirpath = os.path.join(root, dirname)
        items.append(dirpath)


for item in range(len(items)):
    if items[item] not in namesList:
        shutil.move(items[item], archivepath)
        print "Archived ", items[item][len(searchpath) + 1:]
