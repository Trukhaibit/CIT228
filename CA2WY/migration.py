import matplotlib.pyplot as plt  
import numpy as np 
import csv

names = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
interpop20 = []
interpop21 = []
stateinterpop20 = []
stateinterpop21 = []


with open('CA2WY/data/alldata.csv') as f:
    Line_reader = csv.reader(f)

    for row in Line_reader:
        interpop20.append(row[16])
        interpop21.append(row[17])

interpop20 = interpop20[6:]
interpop21 = interpop21[6:]
for r in interpop20:
    stateinterpop20.append(int(r))
for r in interpop21:
    stateinterpop21.append(int(r))

plt.plot(names, stateinterpop20, label="People Immigrating 2020")
plt.plot(names, stateinterpop21, label="People Immigrating 2021")
plt.ylabel('People')
plt.xlabel('States (and DC and Puerto Rico')
plt.title('Immigration Between States and Outside The Country')
plt.legend(loc='best', ncol=2, fontsize=8)
plt.grid()
plt.show()