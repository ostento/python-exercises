def string_reverse(a):
	b = []
	index = 1
	while index <= len(a):
		b.append(a[-index])
		index+=1

	print ''.join(b)

def print_ducklings():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'
	for letter in prefixes:
		if letter == 'O' or letter == 'Q':
			letter += 'u'
		print letter + suffix

def find(word, letter, n):
	index = 0
	word = word[n:]
	while index < len(word):
		if word[index] == letter: 
			return index
		index = index + 1
	return -1

def count(word, letter):
	count = 0
	n = 0
	while find(word, letter, n) != -1:
		count = count + 1
		n = n + find(word, letter, n)+1 # increment n past last instance
	return count

def is_palindrome(a):
	if a == a[::-1]: return True
	else: return False

'''Exercise 8-11: 4 functions which claim to check for lowercase letters.
'''

def any_lowercase1(s):
	'''returns True if the first letter in s is lowercase, False otherwise.'''
	for c in s:
		print c
		if c.islower():
			return True
		else:
			return False

def any_lowercase2(s):
	'''Returns True'''
	for c in s:
		if 'c'.islower():
			return True
		else:
			return False

def any_lowercase3(s):
	'''returns true if the last letter in s is lowercase,false otherwise
	'''
	for c in s:
		flag = c.islower()
	return flag

def any_lowercase4(s):
	'''returns True if any letter is lowercase.'''
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

def any_lowercase5(s):
	'''returns True if any letter is lowercase'''
	for c in s:
		if not c.islower():
			return False
	return True

def rotate_word(s, n):
	'''returns string s, capitalised and 'rotated' thru n alphabetical degrees'''
	result = []
	s = s.upper()
	for c in s:
		d = ord(c)+n
		if d > 90:
			d = d - 25
		if d < 65:
			d = d + 25
		result.append(chr(d))
	return ''.join(result)

def rotate_letter(c, n):
	'''second attempt, after reviewing rotate.py. rotates a single letter through n alphabetical degrees'''
	start = 0

	#conditionally standardises input
	if c.isupper(): start = ord('A')
	elif c.islower(): start = ord('a')
	else: return c

	d = ord(c) - start # gives an index in the range 0 - 25
	result = ((d + n) % 26) + start
	return chr(result)

def rotate_word2(s, n):
	result = []
	for c in s:
		result.append(rotate_letter(c, n))
	return ''.join(result)

print is_palindrome('abaab')