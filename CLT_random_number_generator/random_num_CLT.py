import random
import numpy as np
import scipy, math
import matplotlib.pyplot as plt
import pylab 

random_list = []
random_list_sq = []
def Chi(N):
	for y in range(0,N):
		x_i = random.random()
		random_list.append(x_i)
		chi = sum(random_list)/N

		z = (x_i)**2
		random_list_sq.append(z)
		chi_sq = sum(random_list_sq)/N
		return chi, chi_sq

N2a, N2b = Chi(2)
N3a, N3b = Chi(3)
N4a, N4b = Chi(4)
N10a, N10b = Chi(10)
print (N2a,N2b,N3a,N3b,N4a,N4b,N10a,N10b)

x_exp = N2a +N3a +N4a + N10a
x_exp_sq = N2b + N3b + N4b + N10b 

var_x =x_exp+ x_exp_sq
print (var_x)

plt.plot([2,3,4,10], [N2b,N3b,N4b,N10b], marker = 'o')
plt.plot(var_x)
plt.show()