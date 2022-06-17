#Car Salesman Program
#Calculate subtotal and total of car

print("Car Salesman Program")

#Enter base price

base = input("Please enter price of car. ")
base = int(base)

#Define extra fees (tax, license, dealer prep, dest charge)
#Tax and license a percent of base

dest_charge = 10
dealer_prep = 25
tax = 10 / 100 * base
licens = 5 / 100 * base

#Invoice

print("\n\n\t\t\t~~Your Invoice~~")
print("\n\tBase Price", "\t\t\t$",base)
print("\tDestination Charge", "\t\t$",dest_charge)
print("\tDealer Prep", "\t\t\t$",dealer_prep)
print("\tLicense", "\t\t\t$",licens)
print("\tTax", "\t\t\t\t$",tax)

#Total price

total = dest_charge + dealer_prep + tax + base + licens

print("\t\tTotal Price", "\t\t$",total)


input("\n\n\nPress the enter key to exit.")
