def title():
    print("Your personal calculator")

def main():
    a= int(float(input("Enter your first number:  ")))
    b=int(float(input("Enter your second number:  ")))
    c= int(float(input("Enter your third number:  ")))

    print("Your entered the numbers:", a,b,c)
    print("Your numbers added together= : ", a+b+c)
    print("Your numbers subtracted= : ", a-b-c)
    print("Your numbers multiplied together= :", a*b*c)
    print("your numbers in exponential form=   :", float(int(a**b**c)))
   
    
    try:
        print("Your numbers divided together = :", a/b/c)
        print("Your numbers in integer division form =  :", float(int(a//b//c)))
        print("your numbers in remainder form = : ", int(a%b%c))
    except:
        print("If the second or third number entered =0 division is not allowed")
    return main() 


title()
main()
