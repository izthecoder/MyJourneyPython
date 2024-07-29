is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Waer warm clothes")
else:
    print("It's a lovely day <3")

print("Enjoy your day!")

#e.g 1
price_house = round(1000000,2)
good_credit = False

if good_credit:
    print("Since you have a good credit, down payment only 10%.")
    down_payment = 0.10
else:
    print("Since you have a bad credit, down payment is 20%.")
    down_payment = 0.20
print(f"The down payment is RM{round(price_house * down_payment,2)}")

#e.g. 2
name = input("Enter name: ")

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 10:
    print("Name too long, must be less than 10 characters.")
else:
    print("Name looks good. PLease proceed.")

#e.g. 3
weight = input("Weight: ")
lbs_or_kg = input("(L)bs or (K)g: ")
weight = float(weight)
if lbs_or_kg.upper() == "L":
    print(f"You are {round(weight*0.453592, 2)} Kg.")
elif lbs_or_kg.upper() == "K":
    print(f"You are {round(weight / 0.453592, 2)} pounds.")