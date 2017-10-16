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
	poisson = po(i,5,0.5)
	p_vals1.append(poisson)

p_vals2 = []	
for i in range(0,11): 
	poisson = po(i,10,0.5)
	p_vals2.append(poisson)		