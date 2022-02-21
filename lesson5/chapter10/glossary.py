from asyncio import constants
import json
filename="lesson5/chapter10/glossary.json"
def menu():
    selection = input("1-create file, 2-read file, 3-add to file, 4-quit  ")
    while selection!="1" and selection!="2" and selection!="3" and selection!="4":
        print("You made an invalid selection, please try again")
        selection = input("1-create file, 2-read file, 3-add to file, 4-quit  ")
    return selection
def create(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open(filename, "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")
def append(new_key,new_value):
    with open(filename, "r+") as add_file:
        glossary = json.load(add_file)
        glossary.update({new_key:new_value})
        add_file.seek(0)
        json.dump(glossary, add_file, indent=4, sort_keys=True)
        print("Data has been added to glossary.json")
def read():
    try:
        with open(filename) as read_file:
            glossary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in glossary.items():
            print(key.title() + ":" + value)   
flag = ""
glossary={
    "Tuple":"A fixed-value array",
    "List":"The most flexible collection data type",
    "Dictionary":"Associative array",
    "Append":"To add to the end of something",
    "Key:Value Pair":"Data structure organizing method",
    "Commit":"Confirm changes to",
    "Constant":"An unchanging variable, see variable",
    "Variable":"An adjustable constant, see constant",
    "Print":"Display value or text in terminal",
    ".lower":"Convert all latin characters to lowercase"
}
for g in glossary:
    print(g+":")
    print("\t",glossary[g])
while flag != "4":
    flag = menu()
    if flag == "1":
        create(glossary)
    elif flag == "2":
        read()
    elif flag == "3":
        append(input("What is the name of this item? "),input("What does it mean? "))
    elif flag == "4":
        print("See you soon!")
    else:
        print("Please enter a number between 1-4.")