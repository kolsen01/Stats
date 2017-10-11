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

		#z = (x_i)**2
		#random_list_sq.append(z)
		#chi_sq = sum(random_list_sq)/N
		#return chi, chi_sq

histogram = []
for j in range(0,10000):
	x_j = Chi(2)
	histogram.append(x_j)		


#x_exp = N2a +N3a +N4a + N10a
#x_exp_sq = N2b + N3b + N4b + N10b 

#var_x =x_exp+ x_exp_sq


plt.hist(histogram, bins = None, facecolor = 'g')
plt.title('Random Variables: 2')
plt.xlabel('Average of Random Numbers')
plt.ylabel('Frequency')
plt.axis([0, 1, 0, 10000])

plt.show()