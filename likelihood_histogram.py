import random
import math
import matplotlib.pyplot as plt
import numpy

f = open("decay.txt", "r")
x=[]

for item in f:
	x.append(float(item))

def Tau_avg(N):
	y = []
	for i in range(0,N):
		random.randint(0,1963)
		y.append(x[i])
	avg = numpy.mean(y)
	return avg	

N2 = Tau_avg(2)
N5 = Tau_avg(5)
N10 = Tau_avg(10)
N100 = Tau_avg(100)
N1963 = Tau_avg(1962)

def eq_tau2(N):
	x_val = numpy.linspace(0.1,.7,1000)
	tau = []
	for t in x_val:
		y = (((N)/t)*N100) + N*(math.log(t)) - N - N*(math.log(N100))
		tau.append(y)
	tau_sum=numpy.mean(tau)
	return tau, tau_sum

histogram = []
for j in range(0,100):
	x_j, x_i = eq_tau2(100)
	histogram.append(x_i)	

plt.hist(histogram, facecolor = 'g')
plt.title('Random Variables: 10')
plt.grid(True)

plt.show()