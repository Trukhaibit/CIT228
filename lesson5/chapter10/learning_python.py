filename = "lesson5/chapter10/learning_python.txt"

print("------------Excercise 10-1------------")
with open(filename) as learnFile:
    mylines = learnFile.read()
print("--------Output from read()--------")
print(mylines)

print("--------Output from for loop inside with...open--------")
with open(filename) as learnFile:
    for line in learnFile:
        print(line)

print("--------Output from readlines()--------")
with open(filename) as learnFile:
    mylines = learnFile.readlines()
print("Original list=", mylines)

for line in mylines:
    print(line)

print("------------Excercise 10-2------------")
with open(filename) as learnFile:
    for line in learnFile:
        print("Original: ", line)
        print("Modified: ", line.replace("Python","C#"))