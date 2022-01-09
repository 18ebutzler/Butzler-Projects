import random


player1_score = 0
player2_score = 0

roundinput= input("Enter the number of games you would like to play:")
x=int(roundinput)

player1wins=[]
player2wins=[]

for i in range(x):

   
    player1 = random.randint(1, 6)
    player2 = random.randint(1, 6)
    player1wins.append(player1)
    player2wins.append(player2)
    

    print("Player 1 rolled: ", player1)
    print("Player 2 rolled: ", player2)

    
    if player1 > player2:        
        player1_score = player1_score + 1
    elif player2 > player1:        
        player2_score = player2_score + 1
    

    input("Press enter to continue.")
    
print("End of your games")
print("Player 1 number of wins:", player1_score)
print("Player 2 nnumber of wins:", player2_score)

avg=sum(player1wins)/len(player1wins)
print("The average that player 1 rolled is", round(avg,2))
    

avg2=sum(player2wins)/len(player2wins)
print("the average number player 2 rolled is", round(avg2,2))
    

