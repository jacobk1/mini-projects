'''
RNG guessing game
1/20/2021
'''
import random
from random import seed
from random import randint
from random import shuffle
class GuessNumber() :
   def main() :

   
      def retryn() :             
         print("quitting already? alright")
         import sys
         sys.exit()
         


      def is_prime(a1):
         if a1 > 1:
            for i in range(2, num):
               if (num % i) == 0:
                  print("The number is not prime")
                  break
               else:
                  print("The number is prime")
            else:
               return ("the number is not prime")
            

      def guess() :
         global a1
         try: #checks if inputs are numbers
            g = int(input("take a guess!\n"))
         except ValueError:
            print("invalid entry, plese guess a integer")
            guess()

         if g == a1 :
            win()
         else:
            print("sorry incorrect")
            
            
      def hints():
         global hint,score
         hint =+ hint + 1 #adds one to the hint counter if player asked for one
         score =+ score - (50 * (hint - 1))
         print("your score is now {0}".format(score))
         if hint == 1 :
            if (a1 % 2) == 0 :
               print("Hint: the number is even")
            else :
               print("Hint: the number is odd")
               
         if hint == 2 :
            if (a1 >= 50) :
               print("Hint: the number is greater than or equal to 50")
            else :
               print("Hint: the number is less than 50")
               
         if hint == 3 :
            is_prime()
         if hint == 4 :   
            if a1 >= 50 and a1 <= 75 :
               print("Hint: the number is between 50 and 75")
            elif a1 >= 25 and a1 <= 50 :
               print("Hint: the number is between 25 and 50")
            else :
               print("Hint: the number is not between 25 and 75")
                
         if hint > 4:
            if (a1 >= g + 5) :
               print("the number is atleast 5 greater than your guess")
            elif (a1 <= g - 5) :
               print("the number is at least 5 less than your guess")
            else :
               print("The number is within 5 of your guess") 
         game()                  
                   
                        
      def game():
         global score, tries
         
      #logic if player wants to retry
         print("your score is now {0}".format(score))
         game2()
      
      
      def game2() :
         global tries, retry, score
         while True :
            tries =+ tries + 1
      #ask for player to guess and stores the value as g
            guess ()
      #calculate number of tries and the new score         
            tries =+ tries + 1
            score =+ score - (100 * (tries-1)) #updates score to account for the retry
            h = input("would you like a hint? y/n:\n") #ask play if they want a hint and stores answer as "h"
            if h == "y" :
               hints()   
            elif h == "n" :
               print("Suit Your Self!")
            else :
               print("invalid input, heres a hint")
               hints()
      
      def start_game():
         global score, tries, playagain
         tries = 0
         score = 0
         loopgame()
         
         
         
      def loopgame():
            global hint, a1, score
            score =+ score + 5000
            values = [i for i in range(100)]
            shuffle(values)
            a1 = int(random.choice(values))
            hint = 0
            print("The anwser is a whole number between 0 and 100")
            print(a1) #debug
            game()
         
      
      def win() :
         global score
         if score == (5000 * tries) :#checks if score is perfect
            playagain = input("WOW! Perfect score for {0} tries! your score was {1}. Want to play again for a higher score? y/n \n".format(tries, score))
         else :
            playagain = input("Congratulations your score was {0}! Want to play again for a higher score? y/n \n".format(score))
         if playagain == "n" :
            retry = retryn()
         else:
            loopgame()
      start_game()
   main()
GuessNumber()   