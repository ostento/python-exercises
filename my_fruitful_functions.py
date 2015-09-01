from math import *

def compare(x, y):
	if x > y: return 1
	elif y > x: return -1
	else: return 0

def hypotenuse(a,b):
	return sqrt(a ** 2 + b ** 2)

def is_between(x,y,z):
	return x <= y and y <= z

def ackermann(m, n):
	if m < 0 or n < 0:
		return "ackermann is only defined for m, n > 0"
	elif not isinstance(m, int) or not isinstance(n, int):
		return "ackermann is only defined for positive integers"
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ackermann(m-1, 1)
	elif m > 0 and n > 0:
		return ackermann(m -1, ackermann(m, n-1))

def is_palindrome(a):
	if not isinstance(a, str):
		print ('Only strings can be palindromic')
	if len(a) == 0 or len(a) == 1:
		return True
	elif a[0] != a[-1]: return False
	else: 
		return is_palindrome(a[1:-1])

def is_power(a, b):
	if a == b: return True
	elif a % b == 0 and is_power(a/b, b): return True
	else: return False

def gcd(a, b):
	if b == 0: return a
	else: 
		print 'calling gcd(', b,',', a,'%',b,')'
		return gcd(b, a % b)

print gcd(252, 105)