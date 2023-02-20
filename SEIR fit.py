from scipy.optimize import minimize
from scipy import integrate
import numpy as np
import pylab as pl
import csv

data = []
with open('C:/Users/wan_yib/Desktop/Code/MCM/real test/task 1-1.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        data.append(row)
xdata = [float(t) for t in data[0]]
ydata = [float(i) for i in data[2]]

def fitFunc(sir_values, time, lamda, delta, mu):
    s = sir_values[0]
    e = sir_values[1]
    i = sir_values[2]
    r = sir_values[3]
    N = sir_values[0]+sir_values[1]+sir_values[2]+sir_values[3]

    res = np.zeros((4))
    res[0] = - lamda * s * i / N
    res[1] = lamda * s * i / N - delta * e
    res[2] = delta * e - mu * i
    res[3] = mu * i
    return res

def lsq(model, xdata, ydata, n):
    """least squares"""
    time_total = xdata
    # original record data
    data_record = ydata
    # init t = 0 values + normalized
    I0 = data_record[0]
    S0 = 380000
    E0 = 80000
    R0 = 50000
    N0 = [S0,E0,I0,R0]
    # Set initial parameter values
    param_init = [0.475, 0.00055, 0.001]
    # fitting
    param = minimize(sse(model, N0, time_total, data_record, n), param_init, method="nelder-mead").x
    # get the fitted model
    Nt = integrate.odeint(model, N0, time_total, args=tuple(param))
    # Get the second column of data corresponding to I
    return Nt[:,1]

def sse(model, N0, time_total, data_record, n):
    """sum of square errors"""
    def result(x):
        Nt = integrate.odeint(model, N0, time_total[:n], args=tuple(x))
        INt = [row[1] for row in Nt]
        relativediff = []
        for i in range(n):
            relativediff.append((data_record[i] - INt[i]) / data_record[i])
        difference = np.array(relativediff)
        # difference = np.array(data_record[:n]) - np.array(INt)
        # square the difference
        diff = np.dot(difference, difference)
        return diff
    return result

result = lsq(fitFunc, xdata, ydata, 359)

# Plot data and fit
pl.style.use('seaborn')

pl.clf()
pl.plot(xdata, ydata, "o", label='obversed value')
pl.plot(xdata, result, label='fitting')
pl.xlabel('time/day') 
pl.ylabel('Number of  reported results')
pl.title('SEIR')
pl.legend()
pl.show()