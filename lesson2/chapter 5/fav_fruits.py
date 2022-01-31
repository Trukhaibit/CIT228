fruits=["strawberries","raspberries","bananas"]
for fruit in fruits:
    print("The fruit is", fruit)
    if fruit=="strawberries":
        print("Here's a fun game, try picking out all of the seeds with a pair of tweezers!")
    if fruit=="raspberries": 
        print("Fun to eat, not so fun to pick out of your teeth.")
    if fruit=="bananas":
        print("Technically the only berry on this list.")
    if fruit!="strawberries" and fruit!="raspberries" and fruit!="bananas":
        print("Error!")