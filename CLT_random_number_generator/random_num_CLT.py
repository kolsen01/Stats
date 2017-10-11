import random
import matplotlib.pyplot as plt

def Chi(N):
	random_list_i = []
	for i in range(0,N):
		x_i = random.random()
		z = x_i **2
		random_list_i.append(x_i)
		chi = sum(random_list_i) / N 
	return chi

histogram = []
for j in range(0,10000):
	x_j = Chi(10)
	histogram.append(x_j)	

plt.hist(histogram, bins = 100, facecolor = 'g')
plt.title('Random Variables: 10')
plt.xlabel('Average of Random Numbers')
plt.ylabel('Frequency')
plt.grid(True)

plt.show()