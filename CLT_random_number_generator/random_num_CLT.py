import random
import numpy as np
import scipy, math
import matplotlib.pyplot as plt
import pylab 
import plotly.plotly as py
import plotly.graph_objs as go

random_list_i = []
histogram = []
#random_list_sq = []

def Chi(N):
	counter = 0
	while counter < 1000 :
		counter += 1
		for i in range(0,N):
			x_i = random.random()
			random_list_i.append(x_i)
			chi = (sum(random_list_i))/N 
			histogram.append(chi)

		#z = (x_i)**2
		#random_list_sq.append(z)
		#chi_sq = sum(random_list_sq)/N
		#return chi, chi_sq
		return histogram

N2a = Chi(2)
N3a = Chi(3)
N4a= Chi(4)
N10a = Chi(10)

print (N2a)

#x_exp = N2a +N3a +N4a + N10a
#x_exp_sq = N2b + N3b + N4b + N10b 

#var_x =x_exp+ x_exp_sq
#print (var_x)
#data = [go.Histogram(x=N2a)]
#py.iplot(data, filename='basic histogram')


plt.hist(N2a)
#plt.plot(var_x)
plt.show()