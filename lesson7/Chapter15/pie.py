import matplotlib.pyplot as plt

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
values = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)
wedgeColors=("red","orange","yellow","green","blue")

fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')
plt.suptitle("Popular Graphic Formats on the Web")

plt.show()
