import re
from graphics import *

entries= []

    
   
win=GraphWin("Average", 500,500)
    
   
number = Entry(Point(50,110), 10).draw(win)
numberlab = Text(Point(40,90),"Numbers:").draw(win)

addtolist = Text(Point(150,425), "Add to List").draw(win)
addtolistrec = Rectangle(Point(100,400), Point(200, 450)).draw(win)
calculate = Text(Point(350,425), "Calculate").draw(win)
calculaterec = Rectangle(Point(300,400), Point(400, 450)).draw(win)
average=Entry(Point(50,200),10).draw(win)
averagelab=Text(Point(40,180),"Average:").draw(win)
    


 

def checkValid():
    global number
    text=number.getText()
    pattern=r"[0-9]+"
    if re.fullmatch(pattern,text):
        return int(text)
    else: 
       number.setFill("red")
       return None
    
def calculate():
    average.setText(str(sum(entries)/len(entries)))
    

def calculatebutton(ptr):
    try:
        if ptr.x >= 300 and ptr.x <= 400 and ptr.y >= 400 and ptr.y <= 450:
            return True
        return False
    except:
        return False
 
    
def addtolist():
    value=checkValid()
    if value is not None: 
        entries.append(value)
        number.setText("")
        number.setFill("white")
    
def addtolistclicked(ptr):
    try:
        if ptr.x >= 100 and ptr.x <= 200 and ptr.y >= 400 and ptr.y <= 450:
            return True
        return False
    except:
        return False
 
def main():
    global win
    while True:
        if addtolistclicked(win.checkMouse()):
            addtolist()
            print(entries)
        if calculatebutton(win.checkMouse()):
            calculate()


   

main()

    
         
 
