print("----------------Exercise 3-4----------------")
guests=["Grandma Gerry","Grandma Jean","Grandma Cathey"]
message="will you join us for dinner"

print(f"{guests[0]}, {message}?")
print(f"{guests[1]}, {message}?")
print(f"{guests[2]}, {message}?")

print("----------------Exercise 3-5----------------")
print(guests[2], "couldn't make it!")
del guests[2    ]
guests.insert(2,"Abraham Lincoln")
print(f"{guests[0]}, {message}?")
print(f"{guests[1]}, {message}?")
print(f"{guests[2]}, {message}?")

print("----------------Exercise 3-6----------------")
print("I found a bigger table")
guests.insert(0,"Snap")
guests.insert(2,"Crackle")
guests.append("Pop")
print(f"I am inviting {len(guests)} to dinner")
print(f"{guests[0]}, {message}?")
print(f"{guests[1]}, {message}?")
print(f"{guests[2]}, {message}?")
print(f"{guests[3]}, {message}?")
print(f"{guests[4]}, {message}?")
print(f"{guests[5]}, {message}?")

print("----------------Exercise 3-6----------------")
print("As my dinner table won't be arriving on time, I am unable to invite more than two people to dinner")
badnews="I can no longer invite you to dinner, I am sorry for the inconvenience"
print(guests[0], badnews)
guests.pop(0)
print(guests[1], badnews)
guests.pop(1)
print(guests[2], badnews)
guests.pop(2)
print(guests[2], badnews)
guests.pop(2)
print(f"{guests[0]}, {message}?")
print(f"{guests[1]}, {message}?")
del(guests[1])
del(guests[0])
print("Guests:", guests)