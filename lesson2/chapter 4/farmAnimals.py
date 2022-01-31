animals=["sheep","rabbit","cow","chicken","turkey","pig"]
animalsplus= animals[:]
animalsplus.append("goose")
animalsplus.append("duck")
animalsplus.append("alpaca")
animalsplus.append("goat")

print("------------------Original List------------------")
for animal in animals: {
    print(animal)
}
print("------------------New List------------------")
for animal in animalsplus: {
    print(animal)
}
print("The first three items in the list are:", animalsplus[:3])
print("Three items from the middle of the list are:", animalsplus[4:7])
print("The last three items in the list are:",  animalsplus[-3:])