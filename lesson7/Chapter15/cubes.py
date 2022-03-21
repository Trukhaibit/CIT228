import matplotlib.pyplot as plt

cubed=[]
squared=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num)
    squared.append(num**2)

ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal,cubed, marker=".",c="green",lw="2.0",ls="dashdot")
ax1.set_title("Cubed Numbers")
ax1.set_ylabel("Values Cubed")
ax1.set_xlabel("Input Values")
plt.grid()

ax2 = plt.subplot(1,2,2) 
plt.style.use("seaborn-poster")
ax2.plot(inputVal,squared,color="goldenrod",lw="2",marker="^")
ax2.set_title("Numbers Raised", color="goldenrod")  
ax2.set_ylabel("Second Power")
ax2.set_xlabel("Input Values")
plt.grid()

plt.suptitle("Fun with Numbers",c="green",fontfamily="Comic Sans MS", fontsize="20")
plt.subplots_adjust(top=.8,wspace=1)
plt.show()