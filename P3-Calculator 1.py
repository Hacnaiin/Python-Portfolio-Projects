import math
def calcualtor():
    while True:
        num1=int(input('Enter first number: '))
        num2=int(input('Enter second number: '))
        oper=input('Enter the operator(+,-,/,*) here: ')
        if oper == '+':
            add=num1+num2
            print(add)
            
        elif oper == '-':
            sub=num1-num2
            print(sub)
            
        elif oper == '*':
            mul=num1*num2
            print(mul)
            
        elif oper == '/':
            divi=num1/num2
            print(divi)
        else:
            print('Please enter a valid operator')   

        choice=input('Press E/e to exit or any other key to continue: ')
        if choice =='E' or choice == 'e':
            break
calcualtor()   