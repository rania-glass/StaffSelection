from graphics import *

def showError(message):
    win = GraphWin("Error!", 400, 400);
    win.setBackground("white")

    errorText = Text(Point(win.getWidth()/2, win.getHeight()/2), message)
    errorText.setTextColor("black")
    errorText.draw(win)

    win.getMouse()
    win.close()

    exitText = errorText = Text(Point(win.getWidth()/2, .75*win.getHeight()),
        "Click anywhere to exit.")
