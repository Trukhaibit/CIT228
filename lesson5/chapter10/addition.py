num1 = 0
num2 = 0
flag = ""

while flag != "q":
    flag = ""
    while flag != "1":
        try:
            num1 = int(input("Please enter the first number: "))
            flag = "1"
        except:
            print("I'm sorry, your input wasn't a number.")
            flag = ""
    while flag != "2":
        try:
            num2 = int(input("Please enter the second number: "))
            flag = "2"
        except:
            print("I'm sorry, your input wasn't a number.")
            flag = ""
    print(num1, "+", num2, "=", int(num1) + int(num2))     
    flag = input("Would you like to play again? (type q to quit)")