#----
# EXERCISE 1
#----
import random


def guess_the_number():
    n:int = int(input("Try and guess a number between 0 and 100"))
    result =("Correct","Incorrect")[n == random.randint(0,100)]
    print(f"Your answer is: {result}")
    return


#----
# EXERCISE 2, 3
#----

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

def fib_printer():
    record = []
    while True:
        temp_record = []
        n:int = int(input("Choose a number: "))
        for i in range(n+2):
            fib_i = fib(i)
            if fib_i > n:
                break
            print(fib_i)
            temp_record.append(fib_i)
        record.append(temp_record)
        if input("do you wish to start over?(Y/N): ").lower() == "n":
            break
    print(f"Alle records: {record}")


fib_printer()