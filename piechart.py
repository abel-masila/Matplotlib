import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
working=[2,3,4,3,2]
eating=[7,8,7,2,2]
playing=[8,5,7,8,13]

slices= [7,2,2,13]
activities=['sleeping','working','eating','playing']

cols=['orange','blue','purple','blue']
plt.pie(slices,labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Pie chart')
plt.legend()
plt.show()
