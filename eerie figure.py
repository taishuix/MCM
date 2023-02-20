from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np 
import math

beta=0.692239
omega=1.39134
xi=2.51304
alpha=1.74291

c1 = 2 / (omega * math.sqrt(2*3.14))
c2 = 1/ math.sqrt(2*3.14)

def f_in(t): return c2*math.e**(-t*t/2)

def f_out(x): 
    v, err = integrate.quad(f_in, -100, alpha*(x-xi)/omega)
    return c1*math.e**(-(x-xi)*(x-xi)/(2*omega*omega))*v

X = np.linspace(-2, 8, 1000)
Y = []
for i in range(1000):
    tmpy , erry = integrate.quad(f_out, 0.01*i-2, 0.01*(i+1)-2)
    Y.append(tmpy)
xBar = [1,2,3,4,5,6,7]
yBar = []
for i in range(7):
    if(i==0):
        tmpy , erry = integrate.quad(f_out, -500, 1.5)
    elif(i==6):
        tmpy , erry = integrate.quad(f_out, 6.5, 500)
    else:
        tmpy , erry = integrate.quad(f_out, 0.5+i, 1.5+i)
    yBar.append(tmpy)

plt.style.use('seaborn')
plt.subplot(1,2,1)
plt.plot(X,Y)
plt.xlabel('tries', fontsize = 15)
plt.ylabel('percentage', fontsize = 15)
plt.subplot(1,2,2)
plt.bar(xBar,yBar)
plt.xlabel('tries', fontsize = 15)
plt.ylabel('percentage', fontsize = 15)
print(yBar)
plt.legend(fontsize = 15)
plt.show()