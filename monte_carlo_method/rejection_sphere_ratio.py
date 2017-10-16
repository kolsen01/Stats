# calculates the vratio of the volume of N-sphere inscribed into a unit N-cube to the volume of N-cube
# uses rejection method of monte carlo

import random
import math
import numpy as np

def ratio(N):
	random_list = []
	for i in range(0,N):
		phi = random.random()
		costheta = random.random()
		x = random.random()

		theta = math.acos(costheta)
		r = (x**(1/3))

		x_c = r * math.sin(theta) * math.cos(phi)
		y_c = r * math.sin(theta) * math.sin(phi)
		z_c = r * math.cos(theta)

		vol_cube = x_c * y_c * z_c
		vol_sphere = 4/3*math.pi*(r**3)
		ratio_sc = vol_cube / vol_sphere
		#print (ratio_sc)

		random_list.append(ratio_sc)

		list_ratios =sum(random_list)/N
		#print (list_ratios)

	return list_ratios

list = []
for j in range(0,10):
	N2 = ratio(3)
	list.append(N2)		

print (list)

