def main():
    printIntro()
    probA,probB, n=getInputs()
    winsA,winsB=simNGames(n,probA,probB)
    printSummary(winsA,winsB)
    
def printIntro():
    print("This program simulates a game of rquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indiated by a propabilty (a number bewtween 0 and 1) that")
    print("the player wins the point when serving. player A always")
    print("Has the first serve.")

def getInputs():
    a=float(input("What is the prob. plaer A wins a serve?"))
    b=float(input("What is the prob. player B wins a serve?"))
    n= int(input("How many games to simulate?"))
    return a,b,n

def simNGames(n, probA, probB):
    winsA=winsB=0
    for i in range(n):
        scoreA,ScoreB=simOnegame(probA,probB)
        if scoreA>scoreB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA,winsB


          


def simOneGame(probA,probB):
    serving="A"
    scoreA=0
    scoreB=0
    while not gameOver(scoreA,scoreB):
        if serving =="A":
            if random()< probA:
                scoreA=scoreA+1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB=scoreB+1
            else:
                serving="A"
    return scoreA, scoreB

def gameOver(a,b):
    return a==15 or b==15

def printSummary(winsA,winsB):
    n=winsA+winaB
    print("/nGames simulated:",n)
    print("Wins for A:{0} ({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B:{0} ({1:0.1%})".format(winsB,winsB/n))
    

if __name__=='__main__':main()
        
    
