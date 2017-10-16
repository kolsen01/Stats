# calculates the value of pi using the accept_reject method
# Using the area of a square with the area of a disk inscribed in a square

import random
import math

count_pie = 0;
num = 1000000;

for i in range(0,num):
	x1 = random.random()
	x2 = random.random()
	#Euclidean norm
	calc = math.hypot(x1,x2)
	if calc <=1: 
		count_pie +=1
i+=1

print ('%0.12f' % (4 * count_pie / i))
