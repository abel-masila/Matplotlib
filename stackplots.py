import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
working=[2,3,4,3,2]
eating=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='red',label='Sleeping',linewidth=5)
plt.plot([],[],color='purple',label='working',linewidth=5)
plt.plot([],[],color='orange',label='eating',linewidth=5)
plt.plot([],[],color='blue',label='playing',linewidth=5)
plt.stackplot(days,sleeping,working,eating,playing,colors=['red','purple','orange','blue']);


plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()
