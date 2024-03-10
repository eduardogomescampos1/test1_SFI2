import numpy as np
import csv
from math import sqrt
import sys
import matplotlib.pyplot as plt
from scipy.stats import t, f
from scipy.optimize import curve_fit

#use 's' for running a simple regression according to an specific arbitrary function and 'm' for running a multiple regression with a 6th order polynomial equation

option = sys.argv[1]

def non_linear(x,a,b):
    return a + b*np.power(x,1./3) #Define the arbitrary equation you want to use to attempt a non_linear regression

def non_linear_polynomial(x,a,b,c,d,e,f,g):
    return a + b*x +c*x**2 + d*x**3 + e*x**4 + f*x**5 + g*x**6

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
x = np.array(x)
y = np.array(y)
x = np.ravel(x)
y = np.ravel(y)
if option == 'm':
    x_fix = [[],[],[],[],[],[]];
    for k in range(0,6):
        for j in range(0, len(rows)):
            x_fix[k].append(float(x[j]**(k+1)))
        x_fix[k] = np.array(x_fix[k])
        x_fix[k] = np.ravel(x_fix[k])
    Cov_matrix = [[],[],[],[],[],[]]
    for i in range(0,6):
        for j in range(0,6):
            Cov_matrix[i].append(float(np.sum(x_fix[i]*x_fix[j]) - np.sum(x_fix[i])*np.sum(x_fix[j])/len(rows)))
    Cov_y= []
    for k in range(0,6):
        Cov_y.append(np.sum(y*x_fix[k]) - (np.sum(y)*np.sum(x_fix[k]))/len(rows))
    Cov_y = np.array(Cov_y)
    Cov_y = np.ravel(Cov_y)
    coef = np.linalg.solve(Cov_matrix,Cov_y)
    a = np.average(y)
    print(coef)
    for i in range (0,6):
        a = a - coef[i]*np.average(x_fix[i]) 
    popt, pcov = curve_fit(non_linear_polynomial,x,y)
    plt.scatter(x,y,label = 'Sample data') # x and y will be read from a csv file output by Grafana on the actual project
    plt.plot(x, non_linear_polynomial(x, *popt), 'r-', label= 'Regression')
    plt.savefig('plot.png') 
    print(f"Expected values for a,b,c,d,e,f and g, according to scipy, respectively: {popt}\n") 
    print(f"Expected values for a,b,c,d,e,f and g, according to me, respectively: {a} {coef}\n")
    sqe = np.sum(coef*Cov_y)
    sqt = np.sum(y**2) - ((np.sum(y)**2)/len(rows))
    sqr = sqt - sqe
    print(f"SQE = {sqe}\n")
    print(f"SQR = {sqr}\n")
    print(f"SQT = {sqt}\n")
    s2e = sqe/6
    s2r = sqr/(len(rows) - 7)
    F = s2e/s2r
    print(f"F = {F}\n")
    p_value = f.cdf(F,6,len(rows)-7)
    p_value = 1 - p_value
    if p_value < 0.0001:
        print("The p-value for this test is not significant")
    else:
        print(f"The p-value for this test is {1 - p_value}")
if option == 's':
    popt, pcov = curve_fit(non_linear,x,y)
    plt.scatter(x,y,label = 'Sample data') # x and y will be read from a csv file output by Grafana on the actual project
    plt.plot(x, non_linear(x, *popt), 'r-', label= 'Regression')
    plt.savefig('plot.png') 
    print(f"Expected values for a and b, according to scipy, respectively: {popt}\n")
    x_fix = [np.power(i,1./3) for i in x] # remember to also adapt this for your desired function
    x_fix = np.array(x_fix)
    x_fix= np.ravel(x_fix)
    xy = np.sum(x_fix*y)
    Sxx = np.sum(x_fix**2) - ((np.sum(x_fix)**2)/len(rows))
    Syy = np.sum(y**2) - ((np.sum(y)**2)/len(rows))
    Sxy = xy - ((np.sum(x_fix)*np.sum(y))/len(rows))
    Sr= sqrt((Syy-popt[1]*Sxy)/(len(rows)-2))
    t_calc = (popt[1] - 0)*sqrt(Sxx)/Sr
    t_student = t.isf(0.05,len(rows)-2)
    b_me = Sxy/Sxx
    a_me = np.average(y) - b_me*np.average(x_fix)
    print(f"Expected values for a and b, respectively, according to our model: {a_me} and {b_me}\n")  
    print(f"t-calculated is {t_calc} while its critical value is {t_student}\n")
    p_value = t.sf(np.abs(t_calc),len(rows)-2)*2
    if p_value > 0.0001:
        print(f"p-value is {p_value}\n")
    else:
        print("p-value is not significant")
