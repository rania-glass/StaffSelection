import os
import re
import shutil
from GUI import ErrorMessage, ConfirmationMessage
from Tkinter import Tk
from tkFileDialog import askopenfilename
from Modules import CreateFolders
from Modules import ParseApplications


currentpath = os.path.realpath(__file__)
graphicspath = re.split(r"(.*)\\WelcomeScreen.py", currentpath)
graphicspath = graphicspath[1]
graphicspath = graphicspath+"\\GUI\images"


if os.path.exists("C:\Python27"):
    if os.path.exists("C:\Python27\graphics.py"):
        pass
    else:
        print "Graphics not found"
        print "Installing graphics..."
        shutil.copy(graphicspath+"\graphics.py", "C:\Python27")
        print "Graphics installed"
else:
    print "Please install Python. See the README."

from graphics import *


#shortcut function to create several buttons
#params: color, text, size, location
def button(color, height, width, locationX, locationY):

    rightX = locationX + width
    bottomY = locationY + height
    button = Rectangle(Point(locationX, locationY), Point(rightX, bottomY))
    button.setFill(color)
    button.setOutline(color)
    return button;



def welcome():

    #create the window to place elements into
    win = GraphWin("Super Staff Selection Software!", 800, 800)
    win.setBackground("#FFFFFF")

    #Create the top bar that will serve as a header, including color and text
    #topBar
    topBar = Rectangle(Point(0,0), Point(800, 100))
    topBar.setFill('#0088FF')
    topBar.setOutline('#0088FF')

    #Draw the buzz logo and write the dedication information
    #buzzLogo
    #forTech
    buzzLogo = Image(Point(710, 635), graphicspath+"\\buzz.gif")

    forTech = Text(Point(700, 710), "This software developed for \n Georgia Tech Housing"
        + ": Staff and \n Community Development")
    forTech.setTextColor("gray")
    forTech.setSize(10)

    #Create the settings button
    #settingsText
    settings = button("#BBBBBB", 40, 120, 645, 750)
    settings.draw(win)
    settingsText = Text(Point(705, 770), "Settings")
    settingsText.setTextColor("white")
    settingsText.setSize(14)



    #set welcome text and color
    #message
    message = Text(Point(win.getWidth()/2, 40), "Welcome to "
        + "Super Staff Selection Software!")
    message.setTextColor("white")
    message.setSize(20)


    #Set the helper text above the buttons
    #helpertext
    helpertext = Text(Point(win.getWidth()/2, 160), "Please select an operation"
        + " to be performed on the file.")
    helpertext.setTextColor("gray")
    helpertext.setSize(15)


    #create the buttons
    button1 = button("#0088FF", 75, 250, 268, 195)
    button1.draw(win)
    text1 = Text(Point(394, 228), "Create Applicant Pool")
    text1.setTextColor("white")
    text1.setSize(14)
    text1.draw(win)

    text2 = Text(Point(394, 298), "This will create a folder for each candidate"
        + "\n that contains his or her application.")
    text2.setTextColor("gray")
    text2.setSize(12)
    text2.draw(win)

    button2 = button("#0088FF", 75, 250, 268, 345)
    button2.draw(win)
    text3 = Text(Point(394, 378), "Sort Candidate Files")
    text3.setTextColor("white")
    text3.setSize(14)
    text3.draw(win)
    text4 = Text(Point(394, 468), "This will place the files generated from the input"
        + "\n into the appropriate folder."
        + "\n Recommended for recommendations and \n resumes, cover letters, etc.")
    text4.setTextColor("gray")
    text4.setSize(12)
    text4.draw(win)

    button3 = button("#0088FF", 75, 250, 268, 545)
    button3.draw(win)
    text5 = Text(Point(394, 578), "Organize A File")
    text5.setTextColor("white")
    text5.setSize(14)
    text5.draw(win)
    text5 = Text(Point(394, 468), "This will place the files generated from the input"
        + "\n into the appropriate folder."
        + "\n Recommended for recommendations and \n resumes, cover letters, etc.")
    text5.setTextColor("gray")
    text5.setSize(12)
    text5.draw(win)

    ###
    #Settings
    ###
    #set welcome text and color
    settingsMessage = Text(Point(win.getWidth()/2, 40), "Settings")
    settingsMessage.setTextColor("white")
    settingsMessage.setSize(20)



    topBar.draw(win)
    buzzLogo.draw(win)
    forTech.draw(win)
    message.draw(win)
    settingsText.draw(win)

    while True:
        p1 = win.getMouse()
        if 268 < p1.getX() < 518:
            if 195 < p1.getY() < 270:
                message.undraw()
                info = Text(Point(win.getWidth()/2, 40), "Please select the CSV"
                    + " file that contains the list of candidates.")
                info.setTextColor("white")
                info.setSize(20)
                info.draw(win)
                Tk().withdraw() #keep the root window from appearing
                #Create the directory containing all the candidate folders
                TXTapplist = askopenfilename()
                if ".txt" not in masterList[(len(masterList)-4):]:
                    #show an error message
                    ErrorMessage.showError("Text (.txt) file required.")
                else:
                    ParseApplications(TXTapplist)
                    #perform make directories on this file

            if 295 < p1.getY() < 370:
                print "Call second button function"
            if 395 < p1.getY() < 470:
                print "Call third button function"
            if 495 < p1.getY() < 570:
                print "Call fourth and final button function"

        if 550 < p1.getY() < 590:
            if 645 < p1.getX() < 765:
                print "Settings"

welcome()
