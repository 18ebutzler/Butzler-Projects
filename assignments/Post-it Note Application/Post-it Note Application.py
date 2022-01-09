import re
from graphics import *
from random import choice as rdm_choice

    
   
win=GraphWin("Average", 500,500)
    
   
Title = Entry(Point(50,110), 10).draw(win)
Titlenote = Text(Point(40,90),"Title of Note:").draw(win)

addtolist = Text(Point(150,425), "Save data ").draw(win)
addtolistrec = Rectangle(Point(100,400), Point(200, 450)).draw(win)

note=Entry(Point(50,200),10).draw(win)
notebox=Text(Point(40,180),"note:").draw(win)
    


 

def checkValid():
    global Title
    text=Title.getText()
    pattern="^[a-zA-Z]+$"
    if re.fullmatch(pattern,text):
        return str(text)
    else: 
       Title.setFill("red")
       return None

def checknote():
    global note
    text=note.getText()
    pattern="^[a-zA-Z]+$"
    if re.fullmatch(pattern,text):
        return str(text)
    else:
        note.setFill()
        return None

def savedata():
    global Title
    global note
    #file=open(Title.getText(), "a")
    #file.write("Title " +Title.getText()+ "\n")
    #file.write("The Written note:\n")
    #file.write(note.getText())
    #file.close()
    a=smallerWindow(Title.getText(), note.getText())
    return a
   

class smallerWindow:
    def __init__(self, title, note):
        self.littleWindow=GraphWin("Note", 500,500)
        colors=['purple','red','blue','green','yellow']
        self.littleWindow.setBackground(rdm_choice(colors))
        self.title = Text(Point(40,90),title).draw(self.littleWindow)

        self.close = Text(Point(150,425), "Close ").draw(self.littleWindow)
        self.closeButton = Rectangle(Point(100,400), Point(200, 450)).draw(self.littleWindow)

        self.note=Text(Point(40,180),note).draw(self.littleWindow)
        

#littleWindow=GraphWin("Note", 250,250)
#self.title = Text(Point(40,90),title).draw(littleWindow)

        #close = Text(Point(150,425), "Close ").draw(littleWindow)
        #closeButton = Rectangle(Point(100,400), Point(200, 450)).draw(littleWindow)

        #self.note=Text(Point(40,180),note).draw(littleWindow)  

    

def save(ptr):
    try:
        if ptr.x >= 300 and ptr.x <= 400 and ptr.y >= 400 and ptr.y <= 450:
            return True
        return False
    except:
        return False
 
    
    
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
            savedata()
        


   

main()
