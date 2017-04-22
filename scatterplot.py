import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[9,6,2,1,5,7,3,6,10]
plt.scatter(x,y,label='Scatter1 Plot', color='orange',marker='*',s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()
