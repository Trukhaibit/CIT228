import matplotlib.pyplot as plt
import numpy
import csv

names = []
popdict = {}
pop = []
statepop = []
explode = (.1, 0, 0, 0, 0)
wedgeColors=("purple","blue","green","yellow","orange")

with open('CA2WY/data/alldata.csv') as f:
    Line_reader = csv.reader(f)

    for row in Line_reader:
        popdict[row[7]] = row[4]
        pop.append(row[7])

pop = pop[6:]
for p in pop:
    statepop.append(int(p))
statepop.sort()
statepop = statepop[:5]
for state in statepop:
    names.append(popdict[str(state)])


def absolute_value(val):
    a  = int(numpy.round(val/100.*sum(statepop), 0))
    return a


plt.pie(statepop[:5], explode=explode, labels=names, autopct=absolute_value, shadow=True, startangle=0, colors=wedgeColors)
plt.axis('equal')
plt.suptitle("Bottom Five States (and DC) by Population")

plt.show()

print(statepop)