from scipy.optimize import minimize
from scipy import integrate
import numpy as np
import pylab as pl
import csv

data = []
with open('E:/CS1501H/CUMCM/task 1-1.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        data.append(row)
xdata = [float(t) for t in data[0]]
ydata = [float(i) for i in data[2]]


def fitFunc(sir_values, alpha, beta, gamma):
    n = sir_values[0]
    s = sir_values[1]
    l = sir_values[2]
    m = sir_values[3]
    T = sir_values[0]+sir_values[1]+sir_values[2]+sir_values[3]

    res = np.zeros(4)
    res[0] = - alpha * n * s / T - beta * n * l / T
    res[1] = alpha * n * s / T - gamma * s
    res[2] = beta * n * l / T
    res[3] = gamma * s
    return res


def lsq(model, xdata, ydata, n):
    """least squares"""
    time_total = xdata
    # original record data
    data_record = ydata
    # init t = 0 values + normalized
    N0 = 45000
    S0 = 80000
    L0 = 100
    M0 = 40000
    T0 = [N0, S0, L0, M0]
    # Set initial parameter values
    param_init = [0.047, 0.0001, 0.001]
    # fitting
    param = minimize(sse(model, T0, time_total, data_record, n), param_init, method="nelder-mead").x
    # get the fitted model
    Nt = integrate.odeint(model, T0, time_total, args=tuple(param))
    # Get the second column of data corresponding to I
    return Nt[:,1]


def sse(model, T0, time_total, data_record, n):
    """sum of square errors"""
    def result(x):
        Nt = integrate.odeint(model, T0, time_total[:n], args=tuple(x))
        INt = [row[1] for row in Nt] + [row[2] for row in Nt]
        relativediff = []
        """
        for i in range(n):
            relativediff.append((data_record[i] - INt[i]) / data_record[i])
        difference = np.array(relativediff)
        """

        difference = np.array(data_record[:n]) - np.array(INt)
        # square the difference
        diff = np.dot(difference, difference)
        return diff
    return result


result = lsq(fitFunc, xdata, ydata, 359)

# Plot data and fit
pl.style.use('seaborn')

pl.clf()
pl.plot(xdata, ydata, "o", label='Total')
pl.plot(xdata, result, label='fitting')
pl.legend()
pl.show()

N = 475000