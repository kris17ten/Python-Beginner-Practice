#Word Jumble

import random

#words
WORDS = ("mickey", "minnie", "donald", "daisy", "pluto", "goofy")

#pick a random word
word = random.choice(WORDS)

#if user correct
correct = word

#jumbled version
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#start game
print(
    """
                Welcome to Word Jumble

            Unscramble the letters to make a word.
         (Press the enter key at the prompt to quit.)
"""
    )

print("The jumble is...")
print("\t\t", jumble)

#getting the players guess
guess = input("\nYour guess is: ")

while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess is: ")

#if correct
if guess == correct:
    print("That's it! You guessed it!\n")

input("Press the enter key to exit.")
