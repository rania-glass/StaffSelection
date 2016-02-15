from graphics import *

def showError(message):
    win = GraphWin("Error!", 400, 400);
    win.setBackground("white")

    errorText = Text(Point(win.getWidth()/2, win.getHeight()/2-100), "Error!\n")
    errorText.setSize(28)
    errorText.setTextColor("#FF3300")
    errorText.draw(win)

    messageText = Text(Point(win.getWidth()/2, win.getHeight()/2), message)
    messageText.setSize(20)
    messageText.setTextColor("#222244")
    messageText.draw(win)



    click = win.getMouse()
    while True:
        if click.getX() > 399 and click.getY() > 399:
            win.close()
