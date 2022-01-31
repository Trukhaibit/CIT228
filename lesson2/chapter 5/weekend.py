import datetime
# weekdays tuple
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# retrieving current date
now = datetime.date.today()
# retrieve the day of the week which is an integer
dayOfWeek=now.weekday()
# subscript into weekDay using the weekend
daysToWeekend=6-dayOfWeek
print("There are", daysToWeekend-1, "days until the weekend")
# flag to only print 1 quote in for loop
quotePrinted=False
# prints week days left until weekend with a quote
for left in weekDays[dayOfWeek:6]:
    if today=="Sunday" and quotePrinted==False:
        print(left, "Welcome to a new week!")
        quotePrinted=True
    elif (today=="Monday" or today=="Tuesday" or today=="Wednesday") and quotePrinted==False:
        print(left, "Monday is the only day with an acronym, February 2nd 2022 unfortunatly does not fall on a Tuesday, Wednesday is named after Odin, also known as Wodan.")
        quotePrinted=True
    elif today=="Thursday" and quotePrinted==False:
        print("Thursay is often abrieviated with an H because Tuesday also starts with T, Saturday and Sunday do not follow this rule for whatever reason.")
        quotePrinted=True
    elif quotePrinted==False:
        print("A weekend including Wednesday in favor of Friday has been shown to help make students more productive.")
        quotePrinted=True
    else:
        print(left)