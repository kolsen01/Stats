# calculates the vratio of the volume of N-sphere inscribed into a unit N-cube to the volume of N-cube
# uses rejection method of monte carlo

import random
import math

count_pie = 0;
num = 1000000;

for i in range(0,num):
	x1 = random.random()
	x2 = random.random()
	x3 = random.random()

	#Euclidean norm
	r2 = x1**2 + x2**2 + x3**2
	r = math.sqrt(r2)

	if r2 <=1: 
		count_pie +=1
i+=1

#prints up to 12 decimal places
print ('%0.12f' % (4 * count_pie / i))

