import math

def add(a,b):
    answer=a+b
    print('Addition of ',a, ' and ',b, ' is: ', answer)

def sub(a,b):
    answer=a-b
    print('Subtraction of ',a, ' and ',b, ' is: ',answer)

def mul(a,b):
    answer=a*b
    print('Multiplication of ',a, ' and ',b, ' is: ',answer)

def div(a,b):
    answer=a/b
    print('Divison of ',a, ' and ',b, ' is: ',answer)

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("input your choice: ")

    if choice == 'A' or choice == 'a':
        print('Addition')
        a=int(input('Enter the first number here: '))
        b=int(input('Enter the second number here: '))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a=int(input('Enter the first number here: '))
        b=int(input('Enter the second number here: '))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a=int(input('Enter the first number here: '))
        b=int(input('Enter the second number here: '))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division" )
        a=int(input('Enter the first number here: '))
        b=int(input('Enter the second number here: '))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program Ended!")
        quit()