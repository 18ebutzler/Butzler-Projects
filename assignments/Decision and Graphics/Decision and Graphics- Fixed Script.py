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
    word = input("Enter a 4 letter word with no duplicates ")
    count = 0
    guessesRemaining = 10
    canStart = False
    
    for x in collections.Counter(word):
        #this tells you how many times somethign appears
        count += 1
       
        
    if check.match(word):
        
        if count == 4:
            canStart = True
        
    while not canStart:
        word = input("Enter a 4 letter word with no duplicates ")
        count = 0
        guessesRemaining = 10
        for x in collections.Counter(word):
            count = count + 1
        if check.match(word):
            if count == 4:
                canStart = True
        else:
            guessesRemaining -= 1
            print(guessesRemaining)
    return word.lower()

def isLetter(input1):
    checkL = re.compile("[a-zA-Z]")
    if input1 == "a":
        return True
    elif input1 == "b":
        return True
    if checkL.match(input1):
        return True
    else:
        return False
    
def checkGuess(input1, word):
    count = 0
    for x in word:
        count = count + 1
        if input1.lower() == x:
            return count
    return 0

def show(num, word):
    if num == 1:
        Text(Point(220, 450), word[num-1].upper()).draw(WINDOW)
    elif num == 2:
        Text(Point(280, 450), word[num-1].upper()).draw(WINDOW)
    elif num == 3:
        Text(Point(340, 450), word[num-1].upper()).draw(WINDOW)
    elif num == 4:
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
    lin1 = Line(Point(213, 284), Point(179, 265))
    lin.draw(WINDOW)
    lin1.draw(WINDOW)
def drawLegs():
    lin = Line(Point(213, 335), Point(186, 353))
    lin1 = Line(Point(213, 335), Point(240, 353))
    lin.draw(WINDOW)
    lin1.draw(WINDOW)
#def guessCounter(theguess):
    #label = Text(Point(WINDOW.getWidth() / 2, 2), "Guesses Left: ", theguess.toString())
    
def main():
    label = Text(Point(WINDOW.getWidth() / 2, 50), "You can only guess letters")
    
    guessed1 = False
    guessed2 = False
    guessed3 = False
    guessed4 = False
    badguesscount = 0
    wongame = False
    gameOver = False

    #label1 = Text(Point(WINDOW.getWidth() / 2, 2), "Guesses Left: ", badguesscount)
    
    guessword = getWord()
    drawStage(WINDOW)

    letters=[]

    
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
            badguesscount += 1
            #guessCounter(badguesscount)
            if badguesscount == 1:
                drawHead(WINDOW)
                label1 = Text(Point(WINDOW.getWidth() / 4, 15), "Three guesses remaining")
                label1.draw(WINDOW)

                #guessCounter(badguesscount)
            elif badguesscount == 2:
                drawBody(WINDOW)
                label2 = Text(Point(WINDOW.getWidth() / 4, 30), "Two guesses remaining")
                label2.draw(WINDOW)
                
                #guessCounter(badguesscount)
            elif badguesscount == 3:
                drawArms(WINDOW)
                label3 = Text(Point(WINDOW.getWidth() / 4, 45), "One guess remaining")
                label3.draw(WINDOW)
                
                #guessCounter(badguesscount)
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
            guessed4 = True
            show(4, guessword)
        if guessed1 and guessed2 and guessed3 and guessed4:
            label = Text(Point(WINDOW.getWidth() / 2, 50), "YOU WIN")
            label1 = Text(Point(WINDOW.getWidth() / 2, 75), "Press ANY KEY To QUIT")
            label.draw(WINDOW)
            label1.draw(WINDOW)
    

    if wongame:
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
