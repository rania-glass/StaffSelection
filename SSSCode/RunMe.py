from Tkinter import Tk
from tkFileDialog import askopenfilename
from Modules import CreateFolders
from GUI import ErrorMessage


#Have the user select the file that contains the list of candidates who
#need folders.
Tk().withdraw() #keep the root window from appearing

#Create the directory containing all the candidate folders
masterList = askopenfilename()
if ".csv" not in masterList[(len(masterList)-4):]:
    #show an error message
    ErrorMessage.showError("CSV file required.")

else:
    CreateFolders.createFolders()
    CreateFolders.CreateCandidateFolders(masterList)
