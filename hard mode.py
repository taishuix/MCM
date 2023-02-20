import numpy as np
from matplotlib import pyplot as plt
import csv

data = []
with open('C:/Users/wan_yib/Desktop/Code/MCM/real test/task 1-2.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        data.append(row)
xdata = np.array([float(t) for t in data[0]])
ydata = np.array([float(i) for i in data[1]])
xlogdata = np.log(xdata-174.65403)
predY = -0.09437 + 0.03291 * xlogdata

plt.style.use('seaborn')
plt.plot(xdata,predY,label="y = -0.094 + 0.033 * log (x - 174.65)", c='#274776',linewidth=3.0)
plt.scatter(xdata,ydata,marker='.',c='#8BA9D8')
plt.xlabel('time/day', fontsize = 15)
plt.ylabel('percentage of hardmode/%', fontsize = 15)
plt.legend(fontsize = 15)
plt.show()