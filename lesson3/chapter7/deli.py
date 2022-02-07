sandwich_orders = ["Turkey Reuben","Pastrami","Pastrami","Meat Mountain","Pastrami","Arby Melt","Super Arby","Bacon Beef 'n' Cheddar"]
finished_sandwiches = []
counter = 0
print("The deli has run out of pastrami.")
for sandwich in sandwich_orders:
    if sandwich == "Pastrami":
        counter += 1
while counter > 0 :
    sandwich_orders.remove("Pastrami")
    counter -= 1
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("Sandwiches made today include:")
for sandwich in finished_sandwiches:
    print(sandwich)