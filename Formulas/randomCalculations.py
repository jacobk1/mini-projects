def Fibbinocci(x) :

   f0 = 1 #inital value
   f1 = 1#inital value
   final = 0#final value
   c = 0 #loop counter
   while (x >= c) :
      if (c <= 1) :
         final = 1
      else :
         final = f1 + f0
         f0 = f1
         f1 = final
      c = c + 1
   print(final)

def multipleDice() :
   import random
   D1 = random.randint(1,6)
   D2 = random.randint(1,6)
   D3 = random.randint(1,6)
   D4 = ((D1 + D2 + D3) % 6) + 1
   return D4

def CheckPrime(n):
   from math import sqrt
   from itertools import count, islice
   if n < 2:
        return False

   for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

        else:
            return True