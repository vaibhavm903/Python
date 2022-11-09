''' Solve the following using either while/do while loops
1) Take a number from the user and print sum from 1 to that number 
2) Take a number from the user and print all prime numbers from 1 to that number 
3) Take a number from the user and print all Odd numbers from 1 to that number 
4) Take a number from the user and print all Even numbers from 1 to that number 
5) Take a number from the user and print fibonacci sequence till that number
    eg : fibonnaci sequence for 5 is 0,1,1,2,3,5
    '''
#1) Take a number from the user and print sum from 1 to that number 
def sum_number(number):
    sum = 0
    i = 0
    while i <= number:
        sum = sum + i
        i+=1
    print("Sum is",sum)

#2) Take a number from the user and print all prime numbers from 1 to that number
def prime_number(number):
    i = 1
    print("Printing Prime Numbers::")
    while i <= number:
        
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i,end = " ")
            i += 1
            
        elif i%2 == 0 or i%3 ==0 or i%5 == 0 or i%7 == 0 or i == 1:
            i += 1
            continue
        
        else:
            print(i,end = " ")
            i += 1
            

#3) Take a number from the user and print all Odd numbers from 1 to that number
def odd_number(number):
    i = 1
    print("\nPrinting Odd Numbers::")
    while i <= number:
        print(i,end = " ")
        i += 2

#4) Take a number from the user and print all Even numbers from 1 to that number 
def even_number(number):
    i = 2
    print("\nPrinting Even Numbers::")
    while i <= number:
        print(i,end = " ")
        i += 2     

#5) Take a number from the user and print fibonacci sequence till that number... eg : fibonnaci sequence for 5 is 0,1,1,2,3,5
def fibo(number):
    i = 0
    num1 = 1
    fibs=1
    num2 = 1
    
    print("\nPrinting Fibonacci series::")
    if number == 0:
        print(number)
    else:
        print(i,end = " ")
        print(num1,end = " ")
        
        while fibs <= number:
            print(fibs,end = " ")
            fibs = num1 + num2
            num1 = num2
            num2 = fibs
        


num = int(input("Please enter a number:: "))
sum_number(num)
prime_number(num)
odd_number(num)
even_number(num)
fibo(num)
