from random import randint
from time import clock

def nested_sum(a):
	'''map to reduce (sum) an arbitrary number of nested lists of integers. returns the result in a list.
	'''
	result = [] #acumulator
	for i in range(len(a)):
		result.append(sum(a[i]))
	return result

def capitalize_nested(a):
	'''map to capitalise all strings in all nested lists of a list.'''
	result = [] # accumulator
	for i in a:
		temp = []
		for j in i:
			temp.append(j.capitalize())
		result.append(temp)
	return result

def accum_sum(a):
	''' Input:
				a: a list of integers
		Output:
				result: a list whose ith element = sigma(a[:i])
		'''
	b = a[:] #proper style for list copying, cf copy_list()
	for i in range(len(b)):
		if i == 0: pass
		else: 
			b[i] += b[i-1]
	return b

def copy_list(a):
	'''equivalent to return a[:]!'''
	b = []
	for i in a:
		b.append(i)
	return b

def middle(a):
	'''Input:
				a: a list
		Output:
				result: the list without its 0th and -1th members.
	'''
	b = a[:]
	del b[0]
	del b[-1]	
	return b

def chop(a):
	'''modifies the list a by deleting [0] and [-1]. Returns 'None'
	'''
	del a[0]
	del a[-1]
	return None	

def is_sorted(a):
	'''Returns True if a is composed of sorted elements.
		Precondition: the elements of a can be compared with <, > etc.
		'''
	flag = 0
	for i in a:
		if i > flag: flag = i
		if i < flag: return False
	return True

def is_anagram(m, n):
	'''Returns True if m and n are anagrams (have precisely the same elements).
	'''
	if sorted(list(m)) == sorted(list(n)):
		return True
	else: return False

def has_duplicates(a):
	'''returns True if there are at least two instances of any one value in list a'''
	t = len(a)
	if t <= 1: return False
	i = 0
	while i+1 < t:
		if sorted(a)[i] == sorted(a)[i+1]:
			return True
		i += 1
	return False

def birthday_set(n = 23):
	'''returns a list of n random birthdays in the format [DD,MM]'''
	bdays = []
	for i in range(n): # make months
		bdays.append([randint(1, 12)])
	for i in range(n):
		if bdays[i] in [9,4,6,11]:
			bdays[i].append(randint(1, 30))
		if bdays[i] == 2:
			bdays[i].append(randint(1,28))
		else: bdays[i].append(randint(1,31))
	return bdays

def check_bdays(p = 23, n=100):
	'''checks n sets of birthday_set for identical days. reports the probability of identical birthdays.
	Prerequisites: list t, whose elements are lists in the format [MM, DD]
	Output: Boolean
	'''
	count = 0
	for i in range(n):
		if has_duplicates(birthday_set(p)) == True:
			count += 1
	prob = float(count)/float(n)
	return prob

def remove_duplicates(a):
	'''returns a sorted copy of list a without any duplicates.
	'''
	t = sorted(a)
	for i in range(len(t)-1):
		if t[i] == t[i+1]: del(t[i+1])
	return t

def word_list_app(f):
	'''builds a list from the return-separted entries in a text file with append().'''
	a = open(f)
	t0 = clock()
	res = []
	for i in a:
		res.append(i.strip())
	td = clock() - t0
	return td, res

def word_list_aug(f):
	'''builds a list from the return-separated entries in a text file with augmented assignment. It's extraordinarily slow, presumably because res has to be loaded into memory twice for every for-loop. It would be nice to think of a more efficient way to benchmark it than to let it run thru, tho.'''
	a = open(f)
	t0 = clock()
	res = []
	for i in a:
		res = res + [i.strip()]
	td = clock() - t0
	return td, res


	if len(a) <= 1 and s in a:
		return 1
	elif len(a) <= 1 and s not in a:
		return None
	# else: 
	# 	mid = (high - low)/2
	# 	print mid
	# 	if temp == s: return mid
	# 	if temp[mid] > s: 
	# 		return bisect(temp, s, mid, high)
	# 	if temp[mid] < s: return bisect(temp, s, low, mid)
	# return 'ding'

def bisect(a, s, m, n):
	'''runs a binary search on list a for element s. Returns None if the result isn't found, and the index of the element if it is. This was worked up from the wikipedia page on binary search.

		Preconditions: 
						a should be sorted.
		Input:
						a: a sorted array
						s: the searched-for element
						m: always 0
						n: int = len(a)-1
	'''
	if n < m:
		return None
	else: 
		mid = m + (n-m)/2
		if a[mid] > s: return bisect(a, s, m, mid-1)
		elif a[mid] < s: return bisect(a, s, mid+1, n)
		else: return mid



if __name__ == '__main__':
	a = [[1,2,3],[2, 4, 4]]
	print "Exercise 10.1: a = %r, nested_sum(a) = %r." % (a, nested_sum(a))
	b = [['hurrah', 'hollow','easy'], ['eat','ear', 'eyrie']]
	print "Exercise 10.2: b = %r, capitalize_nested(b) = %r." % (a, capitalize_nested(b))
	print "Exercise 10.3: a[0] = %s, accum_sum(a[0]) = %s." % (a[0], accum_sum(a[0]))
	print "Exercise 10.4: a[0] = %s, middle(a[0]) = %s." % (a[0], middle(a[0]))
	chop(a[0])
	print "Exercise 10.5: a[0] after chop(a[0]) = %s" % a[0]
	print "Exercise 10.6: is_sorted('%s') returns %s. is_sorted(%s) returns %s." % (b[0], is_sorted(b[0][2]), a[1], is_sorted(a[1]))
	print "Exercise 10.7: is_anagram('%s', '%s') returns %s. is_anagram('%s', '%s') returns %s." % (b[0][0], b[0][1], is_anagram(b[0][0], b[0][1]), 'rifle', 'filer', is_anagram('rifle', 'filer'))
	p = 23
	print "Exercise 10.8: the likelihood that %i people share a birthday is approximately %f." % (p, check_bdays(p))
	print "Exercise 10.9: remove_duplicates(%s) returns %s." % (a[1],remove_duplicates(a[1]))
	m = word_list_app('words.txt')
	print "Exercise 10.10: word_list_app(f) returns in %f seconds; word_list_aug(f) returns in about 240s (it's too slow to execute.)" %(m[0])
	a = word_list_app('words.txt')
	l = len(a[1]) -1
	s = b[1][2]
	print "Exercise 10.11: the word '%s' occurs %ith in the word-list." % (s, bisect(a[1], s, 0, len(a[1])-1))
