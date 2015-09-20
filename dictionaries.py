from time import clock
import pronounce 
'''Exercise 10.12 requires the CMU pronouncing library, which is included in this repository, as well as Downey's module 'pronounce.py', also here.'''

def f2dict(f):
	''' Input: 	f: a /n-separated word list
		Output:	a: a dictionary with the words as keys 
	''' 
	fin = open(f)
	a = dict()
	for i in fin:
		a[i.strip()] = None
	return a

def histogram(s):
	''' Counts the frequency of each unique character in the string. Returns a histogram.
		Input:	s: a string
		Output:	h: a histogram contained in a dict()
	'''
	h = dict()
	for c in s:
		h[c] = h.get(c, 0) + 1
	return h

def print_hist(h):
	''' Prints a histogram formatted as a dict().
		Input: 	h, a dict() produced by histogram()
		Output:	Prints a table.
	'''
	sorted_keys = sorted(h.keys())
	for i in sorted_keys:
		print '  ', i,':',h[i],

def reverse_lookup(h, s):
	'''	Checks a dictionary h for keys with values equal to s.
		Input:	h:	a dictionary
				s:	a value to search for.
		Output:	res: a list of all the keys in h which map to s.
	'''
	res = []
	for i in h:
		if h[i] == s:
			res.append(i)
	return res

def inverse_dict(h):
	''' Returns a dict whose keys are the values of h, and whose values are the keys of h.'''
	inverse = dict()
	for i in h: # raises each key sequentially
		inverse.setdefault(h[i], []) # if inverse has no key corresponding to the value h[i], this creates one, and assigns as its value an emptylist.
		inverse[h[i]].append(i)
	return inverse
	
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else: return fib(n-1) + fib(n-2)


known = {0:0, 1:1}

def fib_memo(n):
	if n in known:
		return known[n]
	res = fib_memo(n-1) + fib_memo(n-2)
	known[n] = res
	return res

def fib_test(f, n):
	res = []
	for i in range(n):
		i = i*3
		t0 = clock()
		a = f(i)
		td = t0 - clock()
		res.append([a, td])
	return res

def ack(m,n):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	elif m > 0 and n > 0:
		return ack(m-1, ack(m, n-1))

ack_known = {}

def ack_memo(m, n):
	'''based on the solution.'''
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	try:
		return ack_known[(m,n)]
	except KeyError:
		ack_known[(m,n)] = ack_known[(m,n)] = ack_memo(m-1, ack(m, n-1))
		return ack_known[(m,n)]

def has_duplicates_dict(t):
	lex = {}
	for i in t:
		if i in lex: return True
		lex[i] = True
	return False

def rot_letter(c, n):
	'''rotates a letter c through n values, then returns the rotated character.'''
	if c.isupper(): origin = ord('A')
	elif c.islower(): origin = ord('a')
	else: return c
	index = ord(c) - origin
	res = (index + n) % 26 
	return chr(res + origin)

def rot_word(w, n):
	'''rotates a word w through n values, then returns the rotated word.'''
	res = []
	for c in w:
		res.append(rot_letter(c, n))
	return ''.join(res)

def check_rot_word(s, d):
	'''Checks for all 26 rotations of string s in dict d. Returns a list of matches.'''
	res = []
	for i in range(25):
		rot = rot_word(s, i+1)
		if rot in d: res.append([i+1, ''.join(rot)])
	return res

def rotword_dictscan(d, n):
	'''Checks all 26 rotations of all the words in dictionary d for their 'rotate pairs'. Returns a dict with elements in the format "source: [[rotation, target]]"'''
	res = dict()
	control = 0
	for i in d:
		if control > n: 
			return res
		temp = check_rot_word(i,d)
		if temp: 
			for j in temp: #reformats the return of check_rot_word
				res.setdefault(i, [])
			  	res[i].append(j)
		control += 1
	return res

def cartalk_homophone_check(d, n=100):
	'''Checks a dictionary d for words satisfying the cartalk puzzle: 5-letter words which are homophones with their [1:] and //also// their [0]+[2:] (so to speak).
	'''
	a = pronounce.read_dictionary()
	res = []
	control = 0
	for i in d:
		if control > n: return res
		if len(i) < 5 or i not in a: continue
		m = i[1:]
		if m not in a: continue
		if a[i] == a[m]:
			n = list(i)
			del n[1]
			n = ''.join(n)
			if n not in a: continue
			if a[m] == a[n]: res.append(i)
		control += 1
	return res

if __name__ == '__main__':
	a = f2dict('words.txt')
	b = ['unctuous','olive','spiv']
	t0 = clock()
	c = b[0] in a
	td = clock() - t0
	print 	'Exercise 11.1: %s is a key in the f2dict() of words.txt: %s. Calculated in %f. bisect() takes .5*10^-5' % (b[0], c, td)
	print	'Exercise 11.2: the histogram of %s is %s.' % (b, histogram(b))
	print 	'Exercise 11.3: the histogram from 11.2 ordered by key:',
	print_hist(histogram(b))
	a[b[1]] = b[0]
	print 	"\nExercise 11.4: list of the keys with the value '%s' in our words.txt dict(): %s." % (b[0], reverse_lookup(a, b[0]))
	print 	"Exercise 11.5: the only key with a value of '%s' in our words.txt dict(): '%s'." % (b, inverse_dict(a)[b[0]])
	fib_time = fib_test(fib,5)
	fibm_time = fib_test(fib_memo, 5)
	print 	"Exercise 11.6: normal fib(%i) takes %f; fib_memo(%i) takes %f." % (fib_time[4][0], fib_time[4][1], fibm_time[4][0], fibm_time[4][1])
	print 	"Exercise 11.7: both ack(m,n) and ack_memo(m,n) overflow for values > (3,6)."
	print 	"Exercise 11.8 is left for - a course on cryptography, or a more energetic afternoon."
	e = [1,2,3]
	print 	"Exercise 11.9: has_duplicates_dict(%s) is %s;" % (e, has_duplicates_dict(e)),
	e.append(1)
	print 	"has_duplicates_dict(%s) is %s." % (e, has_duplicates_dict(e))
	f = rotword_dictscan(a,1000)
	print 	"Exercise 11.10: '%s' has the rotwords '%s' (rotated %i) and '%s' (rotated %i)." % (b[2], f[b[2]][0][1], f[b[2]][0][0], f[b[2]][1][1], f[b[2]][1][0])
	g = cartalk_homophone_check(a)
	print 	"Exercise 11.11: the words satisfying the cartalk puzzler are:",
	for i in g[:-1]:
		print i, ',',
	print "and", g[-1],'.'
