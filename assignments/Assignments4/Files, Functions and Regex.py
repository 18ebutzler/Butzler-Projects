
import re
phoneReg = re.compile('\d{3}-\d{3}-\d{4}$')
nameReg = re.compile('[a-zA-Z]+$')
emailReg=re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")

def main():
    ADDBOOKPATH = "addbookFinal.txt"
    ADDBOOKDATA = open("addbook.txt", "r")
    LOGGING = False   



    names=[]
    
    for x in ADDBOOKDATA.readlines():
     names.append(x)
     
    
    newlist=[]
    for x in names:
        newlist.append(x.split(","))

    print(newlist)

    book=[]
    for j in range (len(newlist)):
        test= newlist[j]
        print(test[0])
        print(test[1])
        print(test[2])
        print(test[3])
        if re.match(nameReg,test[0]) and re.match(nameReg,test[1]) and re.match(emailReg, test[2]) and re.match(phoneReg, test[3]):
            print("great")
            book.append(test)
        else:
            print(test, 'was invalid input')
    print(book)
    phonebook=[]
    for i in book:
        i[0]= i[0].capitalize()
        i[1]=i[1].capitalize()
        i[2]=i[2].lower()
        x=','.join(i)
        phonebook.append(x)

    print(phonebook)

    with open('phonebook.txt', 'w') as f:
        for k in phonebook:
            f.write(k)
        
            
main()


        




                    



