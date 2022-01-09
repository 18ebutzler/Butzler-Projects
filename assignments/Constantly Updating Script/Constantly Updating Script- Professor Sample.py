import datetime
from graphics import *
import re
import time

currentselect = 0
addfile = "adds.txt"
mainwin = GraphWin("Address book", 500, 500)
entrywin = GraphWin("Address Entry", 500, 500)
Text(Point(250,50), "Address Book").draw(mainwin)
mainupdate = Text(Point(250,70), "Updating Address book").draw(mainwin)
Text(Point(250,50), "Address Entry").draw(entrywin)
entryfname = Entry(Point(50,110), 10)
entryfnamelab = Text(Point(40,90), "First Name:")
entrylname = Entry(Point(50,150), 10)
entrylnamelab = Text(Point(40,130), "Last Name:")
entryemail = Entry(Point(50,190), 10)
entryemaillab = Text(Point(40,170), "Email:")
entryphone = Entry(Point(50,230), 10)
entryphonelab = Text(Point(40,210), "Phone:")
resettext = Text(Point(150,425), "Reset")
reset = Rectangle(Point(100,400), Point(200, 450))
savetext = Text(Point(350,425), "Save")
save = Rectangle(Point(300,400), Point(400, 450))
nextaddlabel = Text(Point(150,425), "Next")
nextadd = Rectangle(Point(100,400), Point(200, 450))
previousaddlabel = Text(Point(350,425), "Previous")
previousadd = Rectangle(Point(300,400), Point(400, 450))
updatebutton = Rectangle(Point(210,400), Point(290,450))
updatebutton.draw(mainwin)
updatelab = Text(Point(255,425), "Update")
updatelab.draw(mainwin)
nextadd.draw(mainwin)
nextaddlabel.draw(mainwin)
previousadd.draw(mainwin)
previousaddlabel.draw(mainwin)
maindispfname = Text(Point(50,110),"First Name:")
maindisplname = Text(Point(50,130),"Last Name:")
maindispem = Text(Point(70,150),   "Email:")
maindispphone = Text(Point(70,170),"Phone:")
maindispfnamelab = Text(Point(150,110), "")
maindisplnamelab = Text(Point(150,130), "")
maindispemlab = Text(Point(180,156), "")
maindispphonelab = Text(Point(150,170), "")
maindispfname.draw(mainwin)
maindisplname.draw(mainwin)
maindispem.draw(mainwin)
maindispphone.draw(mainwin)
entryfname.draw(entrywin)
entryfnamelab.draw(entrywin)
entrylname.draw(entrywin)
entrylnamelab.draw(entrywin)
entryemail.draw(entrywin)
entryemaillab.draw(entrywin)
entryphone.draw(entrywin)
entryphonelab.draw(entrywin)
reset.draw(entrywin)
resettext.draw(entrywin)
save.draw(entrywin)
savetext.draw(entrywin)
currentaddresses = []
updatedaddresses = []
mainupdate.undraw()


def getnextcheck():
    return datetime.datetime.now() + datetime.timedelta(minutes=1)
def entrysaveclicked(ptr):
    try:
        if ptr.x >= 300 and ptr.x <= 400 and ptr.y >= 400 and ptr.y <= 450:
            return True
        return False
    except:
        return False
def entryreset():
    global entrywin
    global entryfname
    global entrylname
    global entryemail
    global entryphone
    entryfname.setText("")
    entryfname.setFill("white")
    entryemail.setText("")
    entryemail.setFill("white")
    entrylname.setText("")
    entrylname.setFill("white")
    entryphone.setText("")
    entryphone.setFill("white")
def entryresetclicked(ptr):
    try:
        if ptr.x >= 100 and ptr.x <= 200 and ptr.y >= 400 and ptr.y <= 450:
            return True
        return False
    except:
        return False
def updatebook(ptr):
    try:
        if ptr.x >= 210 and ptr.x <= 290 and ptr.y >= 400 and ptr.y <= 450:
            return True
        return False
    except:
        return False
def savedata():
    global addfile
    global entryfname
    global entrylname
    global entryemail
    global entryphone
    file = open(addfile, "a")
    file.write(entryfname.getText()+",")
    file.write(entrylname.getText()+",")
    file.write(entryphone.getText()+",")
    file.write((entryemail.getText()+"\n"))
    file.close()
def checkdata():
    global entryfname
    global entrylname
    global entryemail
    global entryphone
    fname = False
    lname = False
    phone = False
    email = False
    name = re.compile("^[a-zA-Z]+$")
    num = re.compile("^[0-9]{10}$")
    em = re.compile("[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?")
    if name.match(entryfname.getText()):
        fname = True
        entryfname.setFill("white")
    else:
        fname = False
        entryfname.setFill("red")
    if name.match(entrylname.getText()):
        lname = True
        entrylname.setFill("white")
    else:
        lname = False
        entrylname.setFill("red")
    if num.match(entryphone.getText()):
        phone = True
        entryphone.setFill("white")
    else:
        phone = False
        entryphone.setFill("red")
    if em.match(entryemail.getText()):
        email = True
        entryemail.setFill("white")
    else:
        email = False
        entryemail.setFill("red")

    if fname and lname and email and phone:
        return True
    else:
        return False
def pulldata():
    global addfile
    global updatedaddresses
    updatedaddresses = []
    file = open(addfile, "r")
    for x in file:
        updatedaddresses.append(x)
    file.close()
def changedisplay(inp):
    global currentselect
    global maindispfnamelab
    global maindisplnamelab
    global maindispemlab
    global maindispphonelab
    global currentaddresses
    global mainwin
    maindispfnamelab.undraw()
    maindisplnamelab.undraw()
    maindispemlab.undraw()
    maindispphonelab.undraw()

    if inp == 2:
        currentselect = 0
    else:
        currentselect = currentselect+inp
        if currentselect >= len(currentaddresses):
            currentselect = 0
        if currentselect < 0:
            currentselect = len(currentaddresses)-1
    maindispfnamelab.setText(currentaddresses[currentselect].split(",")[0])
    maindisplnamelab.setText(currentaddresses[currentselect].split(",")[1])
    maindispemlab.setText(currentaddresses[currentselect].split(",")[3])
    maindispphonelab.setText(currentaddresses[currentselect].split(",")[2])
    maindispfnamelab.draw(mainwin)
    maindisplnamelab.draw(mainwin)
    maindispemlab.draw(mainwin)
    maindispphonelab.draw(mainwin)
def main():
    global entrywin
    global mainwin
    global mainupdate
    global currentaddresses

    nextpulltime = getnextcheck()
    entryreset()
    pulldata()
    currentaddresses = updatedaddresses
    changedisplay(2)
    # Main Loop
    while True:
        if datetime.datetime.now() > nextpulltime:
            mainupdate.draw(mainwin)
            pulldata()
            nextpulltime = getnextcheck()
            time.sleep(10)
            mainupdate.undraw()

        if entrysaveclicked(entrywin.checkMouse()) or entrywin.checkKey() == "Return":
            if checkdata():
                savedata()
                entryreset()
        if entryresetclicked(entrywin.checkMouse()):
            entryreset()
        if entryresetclicked(mainwin.checkMouse()):
            changedisplay(1)
        if entrysaveclicked(mainwin.checkMouse()):
            changedisplay(-1)
        if updatebook(mainwin.checkMouse()):
            currentaddresses = updatedaddresses
            changedisplay(2)

try:
    main()
except:
    print("Application closed improperly")

