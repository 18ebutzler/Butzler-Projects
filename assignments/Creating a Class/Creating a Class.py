from random import randrange

class Dice:
    def __init__ (self, sides, color):
        if (sides>1):
            self.sides=sides
        else:
            print("has to be greater")
            
        self.color=color
        
    def roll(self):
        num=randrange(1,self.sides+1)
        return num
        
    def getValue(self):
        return Dice.roll(self)

def main():
    dice=Dice(14,"blue")
    print(dice.getValue())

main()
        
        
    
