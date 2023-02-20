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

def fitFunc(sir_values, time, beta, gamma, alpha):
    s = sir_values[0]
    i = sir_values[1]
    r = sir_values[2]
    N = sir_values[0]+sir_values[1]+sir_values[2]

    res = np.zeros((3))
    res[0] = - beta * s * i / N + alpha * r
    res[1] = beta * s * i / N - gamma * i
    res[2] = gamma * i - alpha * r
    return res

def lsq(model, xdata, ydata, n):
    """least squares"""
    time_total = xdata
    # original record data
    data_record = ydata
    # init t = 0 values + normalized
    I0 = data_record[0]
    S0 = 400000
    R0 = 20000
    N0 = [S0,I0,R0]
    # Set initial parameter values
    param_init = [0.05, 0.001,0.001]
    # fitting
    param = minimize(sse(model, N0, time_total, data_record, n), param_init, method="nelder-mead").x
    # get the fitted model
    Nt = integrate.odeint(model, N0, time_total, args=tuple(param))
    March1 = integrate.odeint(model, N0, list(range(450)), args=tuple(param))
    print(March1[418,1])
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
pl.title('SIRS')
pl.legend()
pl.show()