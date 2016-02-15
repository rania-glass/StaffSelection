from graphics import *
import re
import os


currentpath = os.path.realpath(__file__)
graphicspath = re.split(r"(.*)\\ErrorMessage.py", currentpath)
graphicspath = graphicspath[1]
graphicspath = graphicspath+"\images"


def showError(message):
    win = GraphWin("Error!", 400, 400);
    win.setBackground("white")

    #Create the top bar that will serve as a header, including color and text
    #topBar
    topBar = Rectangle(Point(0,0), Point(400, 100))
    topBar.setFill('#0088FF')
    topBar.setOutline('#0088FF')
    topBar.draw(win)

    messageText = Text(Point(win.getWidth()/2, win.getHeight()/2), message)
    messageText.setSize(20)
    messageText.setTextColor("#222244")
    messageText.draw(win)

    #set error header and color
    #message
    error = Text(Point(win.getWidth()/2, 50), "Error!")
    error.setTextColor("white")
    error.setSize(20)
    error.draw(win)

    buzzLogo = Image(Point(335, 345), graphicspath+"\\buzz.gif")
    buzzLogo.draw(win)

    click = win.getMouse()
    while True:
        if click.getX() > 399 and click.getY() > 399:
            win.close()
