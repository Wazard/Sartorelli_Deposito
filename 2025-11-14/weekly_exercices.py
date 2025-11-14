#-----
# EXERCISE 1,2
#-----


# Write an algorithm to find the first prime numbers < N, then print how much time the algorithm took to execute. Then, outputs an execution time record with results
import __init__
from Utilities import wrappers

def is_prime(n: int) -> bool:
    # Return True if n is a prime number, False otherwise.
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility up to sqrt(n)
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6 # Any integer can be written as 6k+r, where r in { 0,1,2,3,4,5}, So primes > 3 must be 6k-1 or 6k+1
    return True

@wrappers.exec_time
def prime_finder(n):
    record = []
    # Handle 2 separately
    if n >= 2:
        record.append(2)
    
    # Check only odd numbers from 3 up to n
    for i in range(3, n + 1, 2):  # step=2 skips evens
        if is_prime(i):
            record.append(i)
    return record

@wrappers.function_printer
def n_prime_numbers():
    record = []
    while True:
        n:int = int(input("Insert a number: "))
        record_tmp = list(prime_finder(n)) # making a list of our Wrapper and prime_finder results
        record_tmp.append( f"input: {n}")
        record.append(record_tmp) 
        if input("Do you want to keep going?(Y/N)").lower() == "n":
            break
    return record

n_prime_numbers()