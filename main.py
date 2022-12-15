#! python3
import math

#calculator
def calculator():
    print("\nWelcome to Calculator")
        # This function adds two numbers 
    def add(x, y):
        return x + y

    # This function subtracts two numbers 
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
       return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    #This function gives squareRoot.
    def sqrt(x):
        return math.sqrt(x)

    #natural Log
    def natlog(x):
        return math.log(x)

    #log to base 10
    def log(x):
        return math.log10(x)

    #power
    def power(x,y):
        return math.pow(x,y)

    #factorial
    def fact(x):
        return math.factorial(int(x))

    def calcMenu():
        print("\nSelect operation:")
        print("1. Add    2. Subtract    3. Multiply    4. Divide    5. Power\n6. Square Root    7. Natural Log    8. Log to base 10    9. Factorial")

        # Take input from the user 
        choice = input("\nEnter choice:")

        if choice == '1':
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
            print("\n",num1,"+",num2,"=", add(num1,num2))

        elif choice == '2':
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
            print("\n",num1,"-",num2,"=", subtract(num1,num2))

        elif choice == '3':
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
            print("\n",num1,"*",num2,"=", multiply(num1,num2))

        elif choice == '4':
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
            if(num2 == 0):
                print("\nDivison by 0 is not defined")
            else:
                print("\n",num1,"/",num2,"=", divide(num1,num2))

        elif choice =='5':
            num1 = int(input("\nEnter base: "))
            num2 = int(input("Enter power: "))
            print("\n",num1,"^",num2,"=", power(num1,num2))

        elif choice == '6':
            num1 = int(input("\nEnter number: "))
            print("\n",num1,"^",0.5,"=", sqrt(num1))

        elif choice == '7':
            num1 = int(input("\nEnter number: "))
            print("\nlog","(",num1,")","=", natlog(num1))

        elif choice == '8':
            num1 = int(input("\nEnter number: "))
            print("\nlog","(",num1,")","=", log(num1))

        elif choice == '9':
            num1 = int(input("\nEnter number: "))
            print("\n",num1,"! =",fact(num1))
            
        else:
            print("Invalid input")
            calculator()
        
        #Again asking user about calculator
        print("\nDo you want to use calculator again?")
        print("1. Yes \t 2. No")
        # Take input from the user 
        choice = int(input("\nEnter choice: "))
        if(choice == 1):
            calcMenu()
        else:
            print("Exitinq...")
            quit()
    calcMenu()

calculator()
