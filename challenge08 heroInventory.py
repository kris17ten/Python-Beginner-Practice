# Hero's Inventory 2.0
# Demonstrates tuples

#create a tuple with some items
inventory = ("sword",
             "armor",
             "sheild",
             "healing potion")

#print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to continue.")

#get the length of a tuple
print("You have", len(inventory), "items in your possession.")

input("\n\nPress the enter key to continue.")

#test for membership with in
if "healing potion" in inventory:
    print("You will fight to live another day.")

#indexing tuples
#display an item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

#display a slice
start = int(input("\nEnter the index number to begin a slice: "))
end = int(input("\nEnter the index number to end a slice: "))
print("inventory[",start,":", end, "] is", end=" ")
print(inventory[start:end])

input("\n\nPress the enter key to continue.")

#concatenating two tuples
chest = ("gold", "gems")
print("You found a chest. It contains:")
print(chest)
print("You add the items to your inventory.")
inventory += chest

print("Your inventory is now: ")
print(inventory)

input("\n\nPress the enter key to exit.")
