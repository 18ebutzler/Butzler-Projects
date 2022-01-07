import re
phonereg = re.compile('\d{3}-\d{3}-\d{4}$')
lettersreg = re.compile('[a-zA-Z]+$')


def main():
    varE=int(input("How many contacts would you like to use: "))
    if varE>0:
            
        contacts=[]
        for i in range (varE):
            varX=input("What is your name:  ")
            if lettersreg.match(varX):
                print("got it")
            else:
                varX=input("What is your damn name: ")
            
            varY=(input("Whats your number:"))
            if phonereg.match(varY):
                print("got it")
            else:
                varY=(input("Whats your number:"))
            
            contacts.append("name: "+ varX+ " number: " +varY)
        print(contacts)
    
       
    else:
        print("It must be a postive number")
        main()



        
main()


