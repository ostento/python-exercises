from math import *

def compare(x, y):
	if x > y: return 1
	elif y > x: return -1
	else: return 0

def hypotenuse(a,b):
	return sqrt(a ** 2 + b ** 2)

def is_between(x,y,z):
	if x <= y and y <= z:
		return True
	else:
		return False

print is_between(1,2,1)