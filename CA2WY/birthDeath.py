import matplotlib.pyplot as plt  
import numpy as np 
import csv

names = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
birth2020 = []
birth2021 = []
death2020 = []
death2021 = []
statebirth2020 = []
statebirth2021 = []
statedeath2020 = []
statedeath2021 = []


with open('CA2WY/data/alldata.csv') as f:
    Line_reader = csv.reader(f)

    for row in Line_reader:
        birth2020.append(row[10])
        birth2021.append(row[11])
        death2020.append(row[12])
        death2021.append(row[13])

birth2020 = birth2020[6:]
birth2021 = birth2021[6:]
death2020 = death2020[6:]
death2021 = death2021[6:]
for r in birth2020:
    statebirth2020.append(int(r))
for r in birth2021:
    statebirth2021.append(int(r))
for r in death2020:
    statedeath2020.append(int(r))
for r in death2021:
    statedeath2021.append(int(r))

plt.scatter(names, statebirth2020, color="lightgreen", label="2020 Births")
plt.scatter(names, statebirth2021, color="green", label="2021 Births")
plt.scatter(names, statedeath2020, color="pink", label="2020 Deaths")
plt.scatter(names, statedeath2021, color="red", label="2021 Deaths")
plt.ylabel('Lives')
plt.xlabel('State')
plt.title('Births/Deaths 2020/2021')
plt.legend(loc='best', ncol=2, fontsize=8)
plt.grid()
plt.show()