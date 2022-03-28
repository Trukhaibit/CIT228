import matplotlib.pyplot as plt  
import numpy as np 
import csv

names = []
ratedict2020 = {}
ratedict2021 = {}
rate2021 = []
staterate2020 = []
staterate2021 = []

with open('CA2WY/data/alldata.csv') as f:
    Line_reader = csv.reader(f)

    for row in Line_reader:
        ratedict2020[row[4]] = row[8]
        ratedict2021[row[9]] = row[4]
        rate2021.append(row[9])

rate2021 = rate2021[6:]
for r in rate2021:
    staterate2021.append(int(r))
staterate2021.sort()
staterate2021 = staterate2021[:15]
for state in staterate2021:
    if ratedict2021[str(state)] == "District of Columbia":
        names.append("DC")
    else:
        names.append(ratedict2021[str(state)])

#Feeds back through names for 2020 info
for name in names:
    if name == "DC":
        staterate2020.append(int(ratedict2020["District of Columbia"]))
    else:
        staterate2020.append(int(ratedict2020[name]))

#Converts to daily average (2020 was a leap year)
for x in range(len(staterate2020)):
    staterate2020[x] = staterate2020[x] / 366
    staterate2021[x] = staterate2021[x] / 365

barWidth=.25
br1 = np.arange(len(names)) 
br2 = [x + barWidth for x in br1]

plt.bar(br1, staterate2020, color ='lightgreen', width=barWidth, label="2020 Population Growth Rate") 
plt.bar(br2, staterate2021, color="pink",  width=barWidth, label="2021 Population Growth Rate")
plt.xticks([r + barWidth for r in range(len(names))],names)

plt.ylabel("Average Population Growth Per Day") 
plt.xlabel("State") 
plt.title("Population Growth 2020/2021 Bottom 15", c="cornflowerblue", fontsize="20") 
plt.legend(loc="best")
plt.show()