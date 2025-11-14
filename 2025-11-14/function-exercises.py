#----
# EXERCISE 1
#----
import random


def guess_the_number():
    n:int = int(input("Try and guess a number between 0 and 100"))
    result =("Correct","Incorrect")[n == random.randint(0,100)] # Ternary operator if n==(random number generated) "correct", else "incorrect"
    print(f"Your answer is: {result}")
    return


#----
# EXERCISE 2, 3
#----

def fib(n): # fibonacci function, {F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2)
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)


def fib_printer(): # function asking for an input n, printing Fib < n
    record = []
    while True:
        temp_record = []
        n:int = int(input("Choose a number: "))
        for i in range(n+2):
            fib_i = fib(i)
            if fib_i > n: # stops the computation if fib > n
                break
            print(fib_i)
            temp_record.append(fib_i) # saving records
        record.append(temp_record)
        if input("do you wish to start over?(Y/N): ").lower() == "n":
            break
    print(f"All records: {record}")


fib_printer()