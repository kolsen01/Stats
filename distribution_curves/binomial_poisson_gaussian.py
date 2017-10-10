import numpy as np
import scipy, math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab 

#binomial distribution
def f(k,n,p):
	y = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
	z = (p**k)*(1-p)**(n-k)
	f = y*z
	return f

b_vals1 = []
for i in range(0,6): 
	binomial = f(i,5,0.5)
	b_vals1.append(binomial)

b_vals2 = []	
for i in range(0,11): 
	binomial = f(i,10,0.5)
	b_vals2.append(binomial)	

b_vals3 = []	
for i in range(0,21): 
	binomial = f(i,20,0.5)
	b_vals3.append(binomial)

#for n = 100 and p = p=0.1, 0.2, 0.5
b_vals4 = []
for i in range(0, 100): 
	binomial = f(i,100,0.1)
	b_vals4.append(binomial)

b_vals5 = []	
for i in range(0,100): 
	binomial = f(i,100,0.2)
	b_vals5.append(binomial)	

b_vals6 = []	
for i in range(0,100): 
	binomial = f(i,100,0.5)
	b_vals6.append(binomial)

#poisson distribution
def po(k,n,p):
	y = (n*p)**k
	x = math.factorial(k)
	z = (math.e)**(-n*p)
	po = (y/x) * z
	return po

p_vals1 = []
for i in range(0,6): 
	poisson = po(i,5,0.5)
	p_vals1.append(poisson)

p_vals2 = []	
for i in range(0,11): 
	poisson = po(i,10,0.5)
	p_vals2.append(poisson)	

p_vals3 = []	
for i in range(0,21): 
	poisson = po(i,20,0.5)
	p_vals3.append(poisson)	

#for n = 100 and p = p=0.1, 0.2, 0.5
p_vals4 = []
for i in range(0, 100): 
	poisson = po(i,100,0.1)
	p_vals4.append(poisson)

p_vals5 = []	
for i in range(0,100): 
	poisson = po(i,100,0.2)
	p_vals5.append(poisson)	

p_vals6 = []	
for i in range(0,100): 
	poisson = po(i,100,0.5)
	p_vals6.append(poisson)	

#gaussain distribution
def ga(k,n,p):
	y = 1/(math.sqrt(2*math.pi*n*p))
	w = (-(k-n*p)**2)/(2*n*p)
	x = (math.e)**w
	ga = y*x
	return ga

g_vals1 = []
for i in range(0,6): 
	gaussian = ga(i,5,0.5)
	g_vals1.append(gaussian)

g_vals2 = []	
for i in range(0,11): 
	gaussian = ga(i,10,0.5)
	g_vals2.append(gaussian)	

g_vals3 = []	
for i in range(0,21): 
	gaussian = ga(i,20,0.5)
	g_vals3.append(gaussian)	

#for n = 100 and p = p=0.1, 0.2, 0.5
g_vals4 = []
for i in range(0, 100): 
	gaussian = ga(i,100,0.1)
	g_vals4.append(gaussian)

g_vals5 = []	
for i in range(0,100): 
	gaussian = ga(i,100,0.2)
	g_vals5.append(gaussian)	

g_vals6 = []	
for i in range(0,100): 
	gaussian = ga(i,100,0.5)
	g_vals6.append(gaussian)			

#Plots for binomial 1
plt.plot(b_vals1, marker='o', color='r', label = 'Binomial')
plt.plot(b_vals2, marker='o', color='b')
plt.plot(b_vals3, marker='o', color='g')
#Plots for binomial 2
plt.plot(b_vals4, marker='o', color='y')
plt.plot(b_vals5, marker='o', color='m')
plt.plot(b_vals6, marker='o', color='k')

#Plots for poisson1
plt.plot(p_vals1, linestyle='--', marker='^', color='r', label = 'Poisson')
plt.plot(p_vals2, linestyle='--', marker='^', color='b')
plt.plot(p_vals3, linestyle='--', marker='^', color='g')
#Plots for poisson2
plt.plot(p_vals4, linestyle='--', marker='^', color='y')
plt.plot(p_vals5, linestyle='--', marker='^', color='m')
plt.plot(p_vals6, linestyle='--', marker='^', color='k')

#Plots for gaussian1
plt.plot(g_vals1, linestyle='--', marker='s', color='r', label = 'Gaussian')
plt.plot(g_vals2, linestyle='--', marker='s', color='b')
plt.plot(g_vals3, linestyle='--', marker='s', color='g')
#Plots for gaussian2
plt.plot(g_vals4, linestyle='--', marker='s', color='y')
plt.plot(g_vals5, linestyle='--', marker='s', color='m')
plt.plot(g_vals6, linestyle='--', marker='s', color='k')

#Details
plt.ylabel('f(k,n,p)')
plt.xlabel('k')

pylab.legend(loc='upper right')
plt.title('Binomial v. Poisson v. Gaussian')
plt.axis([0,70,0,.33])

plt.show()

