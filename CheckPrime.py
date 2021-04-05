'''
Check if a number is prime
From stack exchange
'''
from math import sqrt
from itertools import count, islice
n = int(input("Choose a whole number: "))
def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True
if is_prime(n) == True :
   print(n, "is prime")
else :
   print(n, "is not prime")
    