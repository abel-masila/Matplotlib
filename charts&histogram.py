import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,3,5,9,11]
y2=[7,8,4,2,2]

plt.bar(x,y, label='Bars1',color='Orange')
plt.bar(x2,y2,label='Bars2',color='purple')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bars And Histogram')
plt.legend()
plt.show()
