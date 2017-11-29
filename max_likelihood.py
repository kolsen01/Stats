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

print("N=2:", Tau_avg(2))
print("N=5:", Tau_avg(5))
print("N=10:", Tau_avg(10))
print("N=20:", Tau_avg(20))
print("N=100:", Tau_avg(100))
print("N=1963:", Tau_avg(1963))

N2 = Tau_avg(2)
N5 = Tau_avg(5)
N10 = Tau_avg(10)
N20 = Tau_avg(20)
N100 = Tau_avg(100)
N1963 = Tau_avg(1963)

def plot_tau2(N):
	x_val = numpy.linspace(0.1,.7,1000)
	tau = []
	for t in x_val:
		y = (((N)/t)*N2) + N*(math.log(t)) - N - N*(math.log(N2))
		tau.append(y)
	return x_val, tau

def plot_tau5(N):
	x_val = numpy.linspace(0.1,.5,1000)
	tau = []
	for t in x_val:
		y = (((N)/t)*N5) + N*(math.log(t)) - N - N*(math.log(N5))
		tau.append(y)
	return x_val, tau	

def plot_tau10(N):
	x_val = numpy.linspace(0.1,.5,1000)
	tau = []
	for t in x_val:
		y = (((N)/t)*N10) + N*(math.log(t)) - N - N*(math.log(N10))
		tau.append(y)
	return x_val, tau

def plot_tau20(N):
	x_val = numpy.linspace(0.1,.5,1000)
	tau = []
	for t in x_val:
		y = (((N)/t)*N20) + N*(math.log(t)) - N - N*(math.log(N20))
		tau.append(y)
	return x_val, tau		

def plot_tau100(N):
	x_val = numpy.linspace(0.1,.5,1000)
	tau = []
	for t in x_val:
		y = (((N)/t)*N100) + N*(math.log(t)) - N - N*(math.log(N100))
		tau.append(y)
	return x_val, tau		

a,b = plot_tau2(2)
c,d = plot_tau5(5)
e,f = plot_tau10(10)
g,h = plot_tau20(20)
x,y = plot_tau100(100)

plt.ylim(0,.6)
plt.plot(a,b,'ro')
plt.plot(c,d,'b')
plt.plot(e,f,'g')
plt.plot(g,h,'cyan')
plt.plot(x,y,'black')
plt.grid(True)

plt.show()