#work in progress
#show graphs with mathematica

import random
import math
import matplotlib.pyplot as plt


def ratio(N):
	random_list = []
	for i in range(0,100):
		random.seed(10)
		x = random.random()
		freq = x**2 - x**3
		random_list.append(freq)
		distribution = sum(random_list)/N
	return distribution

histogram = []
for j in range(0,10):
	x_j = ratio(2)
	histogram.append(x_j)

plt.hist(histogram, bins = 10, facecolor = 'g')
plt.title('Random Variables: 10')
plt.xlabel('Average of Random Numbers')
plt.ylabel('Frequency')

plt.show()	
