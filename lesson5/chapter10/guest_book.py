import os
filename="lesson5/chapter10/guest.txt"

if os.path.exists(filename):
    os.remove(filename)

with open(filename, "w") as guestFile:
    guest = input("Please sign into the guestbook with your name: ")
    while guest != "q":
        guestFile.write(guest + "\n")
        print(f"Thank you for visiting us today {guest}!")
        guestFile.write(guest + " had a swell time!\n")
        guest = input("Please sign into the guestbook with your name: (q to quit) ")

with open(filename) as guestFile:
    print("--------All Guests--------")
    for line in guestFile:
        print(line)