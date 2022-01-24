# excercise 1 - use your own first and last name
print("------------------------------------------------")
print("Exercise 1")
name="james olszewski"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is:", name[0].upper())

# exercise 2 - make up your own noun, adjective, verb and ending
# use concatenation to create sentence1
# use f-string to create sentence2
print("------------------------------------------------")
print("Exercise 2")
noun = "salp"
adj = "gelatinous"
verb = "floated"
ending = "away"
sentence1="the " + adj + " little " + noun + " " + verb + " " + ending
sentence2=f"the {adj} little {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())

print("------------------------------------------------")
print("Exercise 3")
longString = """I have heard there are troubles of more than one kind. 
Some come from ahead and some come from behind. 
But I've bought a big bat. I'm all ready you see. 
Now my troubles are going to have troubles with me!"""
print(longString.title())

print("------------------------------------------------")
print("Exercise 4")
print("Jackalope\t\tBigfoot\n")
print("Hide-Behind\t\tDum-Dum\n")
print("Hodag\t\t\tHugag\n")
print("Snallygaster\t\tSnollygoster\n")