import matplotlib.pyplot as plt
from numpy.random import random

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
tempsMin = [39,35,44,48,48,48,45,42,43,46,52,47,50,49,46,49,49,43,46,50,50,52,48,49,47,44,51,47,47,45,48,45,51,53,47,50,53,52,57,57,59,59,58,58,44,42,52,55,52,53,43,41,35,38,39,39,44,47,53,49,50,48,40,38,46,50,57,45,49,55,46,46,45,47,49]
tempsMax = [49,48,51,56,55,51,51,51,49,56,63,56,60,64,57,59,61,56,62,63,67,66,61,62,60,54,61,58,62,59,59,59,61,63,57,63,69,63,72,71,75,74,67,68,59,57,68,63,64,69,56,49,45,53,54,57,52,68,71,70,67,54,51,52,59,66,73,59,66,70,66,58,68,61,61]
date_range=["2021-01-01","2021-01-015","2021-02-01","2021-02-015","2021-03-01"]

print(len(tempsMax))
print(len(tempsMin))
print(len(days))
plt.scatter(days, tempsMin, c=days, cmap=plt.cm.BuPu,label="June Temps")
plt.scatter(days, tempsMax, c=days, cmap=plt.cm.OrRd,label="February Temps")
plt.ylabel('Temps')
plt.xlabel('#Days')
plt.xticks([r*15 for r in range(len(date_range))],date_range)

plt.title('San Francisco Temps (January through March)')
plt.grid()
plt.show()