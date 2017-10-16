#work in progress
#show graphs with mathematica

import random
import math
import matplotlib.pyplot as plt

def ratio(N):
	random_list = []
	for i in range(0,100):
		x = random.random()
		freq = x**2 - x**3
		random_list.append(freq)
		distribution = sum(random_list)/N
	return distribution

def freq(N):
	freq_list = []
	for i in range(0,100):
		y=random.random()
		freq_line = y**2 - y**3
		freq_list.append(freq_line)
		freq_dist = sum(freq_list)/N
	return freq_dist

histogram = []
for j in range(0,10000):
	x_j = ratio(10)
	histogram.append(x_j)

line = []
for k in range(0,100):
	x_k = freq(10)
	line.append(x_k)


fig, ax = plt.subplots(1, 1)
ax2 = ax.twinx()
ax3 = ax2.twiny()

ax3.hist(histogram, bins = 10, facecolor = 'g')
ax.plot(line)
plt.title('Random Variables: 10')
plt.xlabel('Average of Random Numbers')
plt.ylabel('Frequency')

plt.show()	
plt.draw()