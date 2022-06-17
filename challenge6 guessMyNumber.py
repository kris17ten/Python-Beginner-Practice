# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and computer lets
# the player knows if their guess is too high, too low
# or right on the money

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as five attempts. Good luck, smart cookie.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1
#guess in 5 tries
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")
    elif tries == 5:
        print("Oops! Looks like you've run out of tries.")
        print("The number was...", the_number)
        break


input("\n\nPress the enter key to exit.")
