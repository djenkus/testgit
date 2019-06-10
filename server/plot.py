from mpl_toolkits.mplot3d import Axes3D

import numpy as np 
import matplotlib.pyplot as plt 
import csv




with open('idle_power_exynos_1.csv', 'rb') as f:
    reader = csv.reader(f)
    ex1 = list(reader)
with open('idle_power_exynos_2.csv', 'rb') as f:
    reader = csv.reader(f)
    ex2 = list(reader)    
with open('idle_power_exynos_3.csv', 'rb') as f:
    reader = csv.reader(f)
    ex3 = list(reader)
with open('idle_power_exynos_4.csv', 'rb') as f:
    reader = csv.reader(f)
    ex4 = list(reader)
    
print len(ex1), len(ex1[0])    

pdata = []

print(len(ex1))

#for pw in samples:
#	pdata.append(pw)


f = [600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1704,1800,1896,2000,2100]
	
print(f)	
	


pxData = ['0', '1', '2', '3']

px = np.asarray(pxData)

ff = np.asarray(f)

ex11 = np.asarray(ex1)


print(ex11)

result = [[ex11[j][i] for j in range(len(ex11))] for i in range(len(ex11[0]))]

for r in result:
   print(r)
   f



#print(ex1)







fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')






#ax.scatter(x, y, z, c='r', marker='o')

test = []	
	
for exynos in f:
	test.append(0)

tmp = []

print len(ex11), len(ex11[0]) 

#   new_list.append(float(item))

#print(tmp)
	

plt.ylim((0,4))
ax.scatter(f, test, ex1)

#plt.show()
#plt.close(fig)
#plt.close('all')



# surface_plot with color grading and color bar
#ax = fig.add_subplot(1, 2, 2, projection='3d')


#p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, #antialiased=False)
#cb = fig.colorbar(p, shrink=0.5)
