# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:00:11 2024

@author: lempereu
"""

#p161

cache = {3: {}, 4: {},  5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}}
cache[12][9] = 0
cache[12][8] = 0
cache[12][7] = 0
cache[12][6] = 0
cache[12][5] = 0
cache[12][4] = 0
cache[12][3] = 0
cache[12][2] = 0
cache[12][1] = 1
cache[11][9] = 0
cache[11][6] = 0
cache[11][3] = 0
cache[10][9] = 0
cache[10][6] = 0
cache[10][3] = 0
cache[9][9] = 0
cache[9][8] = 0
cache[9][7] = 0
cache[9][6] = 0
cache[9][5] = 0
cache[9][4] = 0
cache[9][3] = 0
cache[9][2] = 0
cache[9][1] = 1
cache[8][6] = 0
cache[8][3] = 0
cache[7][6] = 0
cache[7][3] = 0
cache[6][6] = 0
cache[6][5] = 0
cache[6][4] = 0
cache[6][3] = 0
cache[6][2] = 0
cache[6][1] = 1
cache[5][3] = 0
cache[4][3] = 0
cache[3][3] = 10
cache[3][2] = 3
cache[3][1] = 1


def f(h,w):
	if h*w%3 != 0:
		return 0
	
	if h < w:
		h, w = w, h 
	if h in cache and w in cache[h]:
		return cache[h][w]
	
	r = 0
	#todo : conside the undivisable block possible to build
	
	if w%3==0: # slice horizontally
		for hi in range(1,h//2):
			r += 2*(f(hi, w) + f(h-hi, w))
		if h%2 == 0:
			r += 2*f(h//2, w)
			
	if h%3==0: # slice vertically
		for wi in range(1,w//2):
			r += 2*(f(h, wi) + f(h, w-wi))
		if w%2 == 0:
			r += 2*f(h, w//2)
	
	#Square
	if h == w:
		return r
	return 2*r


print(f(4,3))