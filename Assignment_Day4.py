#******************** Assignment ************************

"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""

'''
def my_calculator(n1,n2):
    ops = input("Please select math operation to perform\nFor Addition Press 1\n For Squaring Press 2\nFor Exponenation Press 3\n::")
    
    match ops:
        case "1":
            print("Addition of given two numbers is:: "+str(n1+n2))
        case "2":
            print(f"Squaring of given two numbers are {n1*n1} and {n2*n2} ")
        case "3":
            print("Exponenation of given two numbers is "+str(n1**n2))
        case _:
            print(r"Invalid Input...!!!  :(")


def my_calculator(n1,n2):
    print("Addition of given two numbers is:: "+str(n1+n2))
    print(f"Squaring of given two numbers are {n1*n1} and {n2*n2} ")
    print("Exponenation of given two numbers is "+str(n1**n2))


'''  


def my_calculator(n1,n2):
    ops = int(input(f"Please select math operation to perform\n1) Addition Press 1\n2) Squaring Press 2\n3) Exponenation Press 3\n::"))
    
    if ops == 1:
        print("Addition of given two numbers is:: "+str(n1+n2))
    elif ops == 2:
        print(f"Squaring of given two numbers are {n1*n1} and {n2*n2} ")
    elif ops == 3:
        print("Exponenation of given two numbers is "+str(n1**n2))
    else:
        print(r"Invalid Input...!!!  :(")

num1 = int(input("Enter the first number:: "))
num2 = int(input("Enter the second number:: "))

my_calculator(num1,num2)
