import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def non_linear(x,a,b):
    return a +b*np.power(x,1./3)

csvreader = csv.reader(open('dumb.csv'))
x = []
y = []
drop = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
for i in rows:
    x.append((i[0]))
    y.append((i[1]))
x = [float(i) for i in x] 
y = [float(i) for i in y]
x_array = x
y_array = y
popt, pcov = curve_fit(non_linear,x_array,y_array)
plt.scatter(x_array,y,label = 'Sample data') # x and y will be read from a csv file output by Grafana on the actual project
plt.plot(x_array, non_linear(x_array, *popt), 'r-', label= 'Regression')
plt.legend()
plt.savefig('plot.png')
print(popt)
