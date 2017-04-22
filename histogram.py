import matplotlib.pyplot as plt

population_ages=[22,26,67,89,90,11,4,1,16,56,23,33,25,30,47,80,100,92,13]
#ids=[x for x in range(len(population_ages))]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()
plt.show()
