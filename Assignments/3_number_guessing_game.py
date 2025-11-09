# A simple number guessing game

import random

number_to_guess = random.randint(1, 100)
guess = None
while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    print("You guessed:", guess)
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")