import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[6,7,8,2,4]
plt.bar(x,y, label='Bars1')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bars And Histogram')
plt.legend()
plt.show()
