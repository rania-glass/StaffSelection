import os
import shutil

#([A-Z][a-z]*)+(.*)([A-Z][a-z]*)+

def sort(path):
    print os.walk(path)
    allfolders = []
    allfiles = []

    for node in os.walk(path):
        (dirpath, dirs, files) = node
        folders = (dirs)
        allfolders.append(dirs)
        allfiles.append(files)



    filestosort = allfiles[0]
    directory = allfolders[0]

    for doc in filestosort:
        for folder in directory:
            if folder in doc:
                newpath = path+"\\"+folder+"\\"+doc
                shutil.move(doc, newpath)
                #os.rename(path, newpath[1])
                print doc, " goes in ", folder
