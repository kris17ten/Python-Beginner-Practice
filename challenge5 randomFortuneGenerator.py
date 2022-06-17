#Fortune Cookie Program
#Fortune generated at random using random library

import random


fortune = random.randint(1,5)
#1 = "Your greatest weakness may turn out to be your greatest asset."
#2 = "Follow your conscience. It's an excellent guide."
#3 = "Keep your friends close and your hunny closer."
#4 = "Forest creatures make great listeners."
#5 = "Be true to your heart."

print("\t\tDisney Fortunes")
print("We all need a little wisdom sometimes.")
print("\nYour fortune for today is...")

if fortune == 1:
    print("\tYour greatest weakness may turn out to be your greatest asset.")
elif fortune == 2:
    print("\tFollow your conscience. It's an excellent guide.")
elif fortune == 3:
    print("\tKeep your friends close and your hunny closer.")
elif fortune == 4:
    print("\tForest creatures make great listeners.")
elif fortune == 5:
    print("\tBe true to your heart.")

print("\nThank you.")

input("\n\nPress the enter key to exit.")
