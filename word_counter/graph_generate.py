from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv
from matplotlib import cm
from matplotlib.ticker import LinearLocator


filename='./time.cvs'
data = []
idx=0
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile) 
    #header = next(csv_reader)       
    
    for row in csv_reader: 
        if idx==0 :
            idx=idx+1 
            continue 

        r = []
        r.append(float(row[2])/(1024 * 1024 * 1024))    

        s = row[4].replace("g","")
        r.append(float(s))    

        r.append(float(row[5]))
        data.append(r)
    
    #print(data)

c0 = [row[0] for row in data]
c1 = [row[1] for row in data]
c2 = [row[2] for row in data]
print(c0)
print(c1)
print(c2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_trisurf(np.array(c0), np.array(c1), np.array(c2),cmap=plt.get_cmap('rainbow'))

ax.set_xlabel('file size/Gb',fontsize=12)
ax.set_ylabel('memory/Gb',fontsize=12)
ax.set_zlabel('time/s',fontsize=12)

plt.show()

# ax.scatter(xs=c0, ys=c1, zs=c2, zdir='z', s=30, c="g", depthshade=True, cmap="jet", marker="^")
# plt.show()
