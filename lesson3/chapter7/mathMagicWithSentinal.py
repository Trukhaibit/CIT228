import random
flag = ""
numberCorrect = 0
while flag != "q":
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer = int(randNumber1 - randNumber2)
    yourAnswer = int(input(f"What is the result of {randNumber1} - {randNumber2}? "))
    if correctAnswer == yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect += 1
    else:
        print("Oops. the correct answer is", correctAnswer)
    flag = input("Type any key to play again (or type q to quit)").lower()
print("You answered", numberCorrect,"questions correctly!")
print("Thanks for playing!")