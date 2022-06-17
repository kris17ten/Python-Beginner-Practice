#Tipper program
#Enter a bill
#Display 15% tip
#Display 20% tip

print("Tipper Program")

bill = input("Please enter your bill amount. ")
bill = int(bill)

fifteen = bill * 0.15
twenty = bill * 0.2

print("Processing...")

print("\n\n15% tip would be:")
print("$",fifteen)

print("\n20% tip would be:")
print("$",twenty)

input("\n\nPress the enter key to exit.")
