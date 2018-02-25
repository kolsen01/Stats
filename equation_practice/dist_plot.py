import numpy as np
import scipy, math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab 

def r2(x) :
    n = 38.213 + 127.918*x + 311.809*x**2 + 134.792*x**3  #where coefficients were calculated above 
    return n

#given values
theta_i = [-0.9,-0.7,-0.5,-0.3,-0.1,0.1,0.3,0.5,0.7,0.9]
y_j = [82.0,50.0,35.0,27.0,26.0,60.0,108.0,188.0,319.0,519.0]

#calculated from n
n_j = []
chi_sq = []

a=0 #initialize
b=0	#initialize

for z in theta_i:
    n_j.append(r2(z)) #add expected values to array

er = []
for i in range(0,10):
	x = math.sqrt(y_j[i])
	er.append(x)


plt.plot(theta_i, n_j, marker='o', color='r', label = 'r=3')
plt.plot(theta_i, y_j, marker='*', color='b', label="data")

#Details
plt.ylabel('y_j')
plt.xlabel('theta_i')

plt.errorbar(theta_i, n_j, yerr=er, label='error')

pylab.legend(loc='upper left')
plt.title('Polynomial r=3 Test Fit')

plt.show()
