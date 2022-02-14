from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))

d6 = Die()
d10 = Die(10)
d20 = Die(20)
print("D six")
for x in range(10):
    d6.roll_die()
print("D ten")
for y in range(10):
    d10.roll_die()
print("D twenty")
for z in range(10):
    d20.roll_die()