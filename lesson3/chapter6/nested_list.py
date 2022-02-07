pizza={
    "Jason M":["Pepperoni","Sausage","Ham"],
    "Jessica M":["Pineapple","Ham"],
    "Carley R":["No Cheese","Olives","Peppers"]
}

for p in pizza:
    print(p)
    for i in pizza[p]:
        print("\t"+i)