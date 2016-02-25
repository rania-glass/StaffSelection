import os
import re
import csv
import shutil
from GUI import ConfirmationMessage

currentpath = os.path.realpath(__file__)
directorypath = re.split(r"(.*)\\SSSCode\\Modules\\CreateFolders.py", currentpath)
directorypath = directorypath[1]


#Create the directory containing all the candidate folders
#param masterList is the CSV file that contains the candidates names

def createFolders(masterList):
    #write to the output directory
    directory = directorypath + "\\SSSCodeTestingMaterial\StaffSelectionOutput"
    if not os.path.exists(directory + "\Male"):
        os.makedirs(directory + "\Male")
    else:
        pass
    if not os.path.exists(directory + "\Female"):
        os.makedirs(directory + "\Female")
    else:
        pass

    with open(masterList) as selected:
        reader = csv.reader(selected)
        selectedList = list(reader)

        for i in selectedList:
            if i[2] is "M":
                if not os.path.exists(directory + "\Male\\" + i[0] + ", " + i[1]):
                    os.makedirs(directory + "\Male\\" + i[0] + ", " + i[1])
                else:
                    pass
            elif i[2] is "F":
                if not os.path.exists(directory + "\Female\\" + i[0] + ", " + i[1]):
                    os.makedirs(directory + "\Female\\" + i[0] + ", " + i[1])
                    ConfirmationMessage.showConfirmation("A folder was created for each "
                        + "candidate in that list.")
                else:
                    ConfirmationMessage.showConfirmation("Folders for those candidates"
                        + " already exist.")
                    pass
