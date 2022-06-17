#No Vowels
#Demonstrates creating new strings with a for loop

message = input("Enter your message: ")
new_message = ""
vowels = "aeiou"

print()
for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
        print("A new string has been created:", new_message)

print("\nYour message without vowels is: '", new_message, "'")

input("\n\nPress the enter key to exit.")
