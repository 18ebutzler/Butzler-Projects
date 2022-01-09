from graphics import *
import re
import collections

WINDOW = GraphWin("Hang Man", 500, 500)


def drawStage(win):
    baseP1x = 5
    baseP1y = 490
    baseP2x = 150
    baseP2y = 430
    base = Rectangle(Point(baseP1x, baseP1y),
                     Point(baseP2x, baseP2y))
    base.setFill("black")
    pole = Rectangle(Point((baseP1x+baseP2x)/2-10, (baseP1y+baseP2y)/2),
                     Point((baseP1x+baseP2x)/2+10, (baseP1y+baseP2y)/2-350))
    pole.setFill("black")
    toppole = Rectangle(Point((baseP1x+baseP2x)/2, (baseP1y+baseP2y)/2-350),
                        Point((baseP1x+baseP2x)/2+150, (baseP1y+baseP2y)/2-325))
    toppole.setFill("black")
    rope = Line(Point((((baseP1x+baseP2x)/2+(baseP1x+baseP2x)/2+150))/2+60, (baseP1y+baseP2y)/2-325),
                Point((((baseP1x+baseP2x)/2+(baseP1x+baseP2x)/2+150))/2+60, (baseP1y+baseP2y)/2-250))

    Line(Point(200, 460), Point(240, 460)).draw(win)
    Line(Point(260, 460), Point(300, 460)).draw(win)
    Line(Point(320, 460), Point(360, 460)).draw(win)
    Line(Point(380, 460), Point(420, 460)).draw(win)
    toppole.draw(win)
    base.draw(win)
    pole.draw(win)
    rope.draw(win)
def getWord():
    check = re.compile("^[a-zA-Z]{4}$")
    word = input("Enter a 4 letter word with no duplicates")
    count = 0
    canStart = False
    for x in collections.Counter(word):
        count = count+1
    if check.match(word):
        if count == 4:
            canStart = True
    while not canStart:
        word = input("Enter a 4 letter word with no duplicates")
        count = 0
        for x in collections.Counter(word):
            count = count + 1
        if check.match(word):
            if count == 4:
                canStart = True
    return word.lower()
def isLetter(input):
    checkL = re.compile("[a-zA-Z]")
    if input == "a":
        return True
    elif input == "b" or input == "B":
        return True
    if checkL.match(input):
        return True
    else:
        return False
def checkGuess(input, word):
    count = 0
    for x in word:
        count = count + 1
        if input.lower() == x:
            return count
    return 0
def show(num, word):
    if num == 1:
        Text(Point(220, 450), word[num-1].upper()).draw(WINDOW)
    elif num == 2:
        Text(Point(280, 450), word[num-1].upper()).draw(WINDOW)
    elif num == 4:
        Text(Point(340, 450), word[num-1].upper()).draw(WINDOW)
    elif num == 3:
        Text(Point(400, 450), word[num-1].upper()).draw(WINDOW)
    else:
        print("You should never see this")
def drawHead(win):
    cir = Circle(Point(213, 230), 20)
    cir.draw(win)
def drawBody(WINDOW):
    lin = Line(Point(213,250), Point(213, 335))
    lin.draw(WINDOW)
def drawArms(WINDOW):
    lin = Line(Point(213, 284), Point(247, 265))
    lin1 = Line(Point(213, 190), Point(179, 265))
    lin.draw(WINDOW)
    lin1.draw(WINDOW)
def drawLegs():
    lin = Line(Point(213, 335), Point(186, 353))
    lin1 = Line(Point(213, 335), Point(240, 265))
    lin.draw(WINDOW)
    lin1.draw(WINDOW)
def main():
    label = Text(Point(WINDOW.getWidth() / 2, 50), "You can only guess letters")
    guessed1 = False
    guessed2 = False
    guessed3 = False
    guessed4 = False
    badguesscount = 0
    wongame = False
    gameOver = False
    guessword = getWord()
    drawStage(WINDOW)
    while not gameOver:
        guessletter = WINDOW.getKey()
        validguess = isLetter(guessletter)
        while not validguess:
            label.draw(WINDOW)
            guessletter = WINDOW.getKey()
            validguess = isLetter(guessletter)
            label.undraw()

        checkstat = checkGuess(guessletter, guessword)
        if checkstat == 0:
            badguesscount = badguesscount + 1
            if badguesscount == 1:
                drawHead(WINDOW)
            elif badguesscount == 2:
                drawBody(WINDOW)
            elif badguesscount == 3:
                drawArms(WINDOW)
            else:
                drawLegs()
                gameOver = True
        elif checkstat == 1:
            guessed1 = True
            show(1, guessword)
        if checkstat == 2:
            guessed2 = True
            show(2, guessword)
        if checkstat == 3:
            guessed3 = True
            show(3, guessword)
        if checkstat == 4:
            show(4, guessword)
        if guessed1 and guessed2 and guessed3 and guessed4:
            wongame = True
            gameOver = True

    if wongame:
        label = Text(Point(WINDOW.getWidth() / 2, 50), "YOU WIN")
        label1 = Text(Point(WINDOW.getWidth() / 2, 75), "Press ANY KEY To QUIT")
        label.draw(WINDOW)
        label1.draw(WINDOW)
    else:
        label = Text(Point(WINDOW.getWidth() / 2, 50), "YOU LOSE")
        label1 = Text(Point(WINDOW.getWidth() / 2, 75), "Press ANY KEY To QUIT")
        label.draw(WINDOW)
        label1.draw(WINDOW)
    WINDOW.getKey()
    WINDOW.close()

try:
    main()
except GraphicsError:
    print("Closed manually")
