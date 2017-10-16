import numpy as np
import scipy, math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab 

#for n=100,1000 and p=.5

#binomial distribution
def f(k,n,p):
	y = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
	z = (p**k)*(1-p)**(n-k)
	f = y*z
	return f

b_vals1 = []
for i in range(0,6): 
	binomial = f(i,100,0.5)
	b_vals1.append(binomial)

b_vals2 = []	
for i in range(0,11): 
	binomial = f(i,1000,0.5)
	b_vals2.append(binomial)	

#poisson distribution
def po(k,n,p):
	y = (n*p)**k
	x = math.factorial(k)
	z = (math.e)**(-n*p)
	po = (y/x) * z
	return po

p_vals1 = []
for i in range(0,6): 
	poisson = po(i,100,0.5)
	p_vals1.append(poisson)

p_vals2 = []	
for i in range(0,11): 
	poisson = po(i,1000,0.5)
	p_vals2.append(poisson)	

#gaussain distribution
def ga(k,n,p):
	y = 1/(math.sqrt(2*math.pi*n*p))
	w = (-(k-n*p)**2)/(2*n*p)
	x = (math.e)**w
	ga = y*x
	return ga	

g_vals1 = []
for i in range(0,6): 
	gaussian = ga(i,100,0.5)
	g_vals1.append(gaussian)

g_vals2 = []	
for i in range(0,11): 
	gaussian = ga(i,1000,0.5)
	g_vals2.append(gaussian)

#Plots for binomial 1
plt.plot(b_vals1, marker='o', color='r', label = 'Binomial')
plt.plot(b_vals2, marker='o', color='b')

#Plots for poisson1
plt.plot(p_vals1, linestyle='--', marker='^', color='r', label = 'Poisson')
plt.plot(p_vals2, linestyle='--', marker='^', color='b')

#Plots for gaussian1
plt.plot(g_vals1, linestyle='--', marker='s', color='r', label = 'Gaussian')
plt.plot(g_vals2, linestyle='--', marker='s', color='b')

#Details
plt.ylabel('f(k,n,p)')
plt.xlabel('k')

pylab.legend(loc='upper right')
plt.title('Binomial v. Poisson v. Gaussian')
plt.axis([0,70,0,.33])

plt.show()


