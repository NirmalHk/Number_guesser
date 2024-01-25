import random
numbers=list(range(1,101))
from art import logo
#from replit import clear
print(logo)

guess = random.choice(numbers)
print(f"psst, the correct guess is {guess}")
easy = 10
hard = 5



difficulty = input("Do you want to the easy or hard difficulty? ").lower()
if difficulty == 'easy':
  lives = 10
elif difficulty == 'hard':
  lives = 5



while lives > 0:
  print(f"you have like {lives} lives left.")
  user_guess = int(input("What is you guess?"))
  
  if user_guess == numbers[guess-1]:
    print("You got it!.")
    lives =0
    #clear()
  elif user_guess >numbers[guess-1]:
    print("Too high.")
    lives -= 1
  elif user_guess < numbers[guess-1]:
    print("Too low.")
    lives -= 1
print("Game Over!")
