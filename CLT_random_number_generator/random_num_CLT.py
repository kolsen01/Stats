import random
import numpy as np
import scipy, math
import matplotlib.pyplot as plt
import pylab 

random_list_i = []
random_list_j = []
#random_list_sq = []

def Chi(N):
	for i in range(0,N):
		x_i = random.random()
		x_j = random.random()
		random_list_i.append(x_i)
		random_list_j.append(x_j)
		chi = (sum(random_list_i) + sum(random_list_j))/N 

		#z = (x_i)**2
		#random_list_sq.append(z)
		#chi_sq = sum(random_list_sq)/N
		#return chi, chi_sq
		return chi

N2a, N2b = Chi(3)
N3a, N3b = Chi(4)
N4a, N4b = Chi(6)
N10a, N10b = Chi(11)

print (N2a,N2b,N3a,N3b,N4a,N4b,N10a,N10b)

#x_exp = N2a +N3a +N4a + N10a
#x_exp_sq = N2b + N3b + N4b + N10b 

var_x =x_exp+ x_exp_sq
print (var_x)

plt.plot([2,3,4,10], [N2b,N3b,N4b,N10b], marker = 'o')
#plt.plot(var_x)
plt.show()