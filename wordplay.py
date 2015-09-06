from itertools import *
import string

def avoids(word, s):
	flag = True
	for c in word:
		for d in s:
			if c.upper() == d.upper(): flag = False
	return flag

def lettercheck(file, letters = '', report = False):
	'''checks a user-inputted string of letters against a wordlist, returning the percentage of the wordlist which contains none of those letters. if report is True it also prints a report.
		input: 
				file: a wordlist
				raw: a string containing letters
		output:
				prints an array of matching words and the percentage they form of the wordlist.
		'''
	if letters == '':
		letters = raw_input('Enter letters to avoid: ') # takes input if not already provided
	s = '' 
	for c in letters: #cleans up the input
		if c.isalpha() and avoids(s, c): s = s + c #builds the comparison-string, excluding multiples
	fin = open(file)
	result = [] #initialising...
	count = 0
	for line in fin: #iterates the file
		count += 1 #gives the number of words
		word = line.strip() #eliminates formatting
		if avoids(word, s): 
			result.append(word)
	percentage = (len(result)*100.0)/count
	if report == True:
		print result
		print "%r percent of words in the file did not contain any of the letters in '%s'" % (percentage, s)
	return percentage



def word_minmax(f, n):
	'''parses a file and returns a string s of n characters s.t. lettercheck(file, s) returns the largest possible value.
			input:
					file: a wordlist
					n: the length of the string to pass to lettercheck()
			returns:
					s: the optimal string

		For the task specified by the exercise (optimal set of 5 abecedarian characters) this program is far too slow. there are ~65000 unique (index-ambivalent) combinations, which requires ~ 65000 executions of lettercheck. several hours of execution at least. Probably can't be computationally fixed.
	'''
	best_list = []
	result = 0.0
	a = string.ascii_lowercase
	for i in  combinations(list(a), n):
		strung = ''.join(i)
		temp = lettercheck(f, strung)
		if temp > result:
			result = temp
			best_list = strung
			print "\n Current best: %r AND %r selects %r of %r \n" % (f, best_list, result, f)
		else: print strung, ', not better.' ,
	return best_list



def word_minmax2(f, n, v=False):
	'''second effort at word_minmax, working on the (slightly dubious?) assumption that the optimal string will be composed of optimal letters, so that the n best letters will form the least-exclusive n-lengthed string.
		
		input:
				file: a wordlist
				n: the length of the desired optimal string
				v: verbosity
		returns:
				s: the optimal string
	'''
	result = []
	for i in range(n): #build a container for the result. Array of n tuples, listing the best characters and the percentage of the wordlist they excluded.
		result.append([100.0,''])
	letters = string.ascii_lowercase
	for c in letters:
		percentage = lettercheck(f, c)
		if percentage < result[0][0]:
			result[0][0] = percentage
			result[0][1] = c
			result = sorted(result, reverse=True)
			if v == True:
				print result
	result_string = ''
	sum_of_percentages = 0.0
	for i in range(n):
		result_string += result[i][1]
		sum_of_percentages += result[i][0]
	average = sum_of_percentages / n
	
	if v == True:
		print "The optimal string, %s, was composed of letters which included an average %f percent of the wordlist. The actual percentage of words excluded by the string as a whole was %f percent." % (result_string, 100-average, lettercheck(f, result_string))

	return result_string

def uses_only(word, s):
	'''Returns True if the word is composed only of characters in the string 's'
		input:
				word: an alphabetical string
				s: an alphabetical comparison-string
		output:
				Boolean
	'''
	if word == '':
		return True
	else:
		if uses_only(word[:-1], s) and word[-1] in s:
			return True
		else: return False

def uses_all(word, s):
	'''Returns True if the word uses each of the characters in s at least once.
	'''
	s_range = range(len(s))
	s_list = []
	for i in s_range: # make a new list in which every character of s is assigned a boolean flag
		s_list.append([s[i], False])

	for j in s_list: #for every character in the testing string
		if j[1] == False and word.find(j[0]) != -1: #if the flag of the character from s hasn't already been set True, and can be found in the test-word...
			j[1] = True # set that character's flag to 'True'

	flag = True

	for j in s_list:
		if not j[1]: flag = False

	return flag

def uses_all2(word, s):
	'''rewrite after checking the solutions. Returns True if the word uses each of the characters in s at least once.'''
	if s == '':
		return True
	else: 
		if uses_all2(word, s[:-1]) and s[-1] in word:
			return True
		else: return False

def uses_all3(word, s):
	'''the solution code.'''
	for letter in s:
		if letter not in word:
			return False
	return True

def is_abecedarian(word):
	'''returns True if the letters in word are in abecedarian order. 'aa' is True.'''
	position = 'a'
	for i in word:
		if i >= position:
			position = i
		else: return False
	return True

def is_abecedarian_r(word):
	'''the book's recursive solution for abc'ian. note that it steps forward thru the word: I've acquired a habit always to step backwards when recursing.'''

	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarian_r(word[1:])


def filter_list(f, fin, s=''):
	'''Returns a subset of wordlist fin, filtered by function f (optionally, with string 's' passed to it.)
		input:
				fin: a wordlist
				f: a function
				s: a string of characters
		output: 
				returns a list of words, the number of these words, and the magnitude of their superset.
	'''
	wordlist = open(fin) # import the wordlist
	result = [] # initialise the result variable
	count_sub = 0
	count_super = 0
	for line in wordlist:
		count_super += 1
		word = line.strip() # clean the word
		if s:
			if f(word, s):
				result.append(word)
				count_sub += 1
		else: 
			if f(word):
				result.append(word)
				count_sub += 1
	return result, count_sub, count_super

def ispair(string):
	'''takes a pair of characters and returns true if they're identical'''
	if string[0]==string[1]:
		return True
	else: return False

def car_talk(word):
	'''checks word for the presence of any three consecutive pairs of letters (ie eellkk). Returns True if the word contains such a set of characters, False otherwise.
	input:
			word: an alphabetical string
	'''
	a = len(word)
	for i in range(a-1):
		if a - i < 6: return False
		if ispair(word[i]+word[i+1]) and ispair(word[i+2]+word[i+3]) and ispair(word[i+4]+word[i+5]):
			return True
	return False

def has_palindrome(word, start, len):
	'''rewrite of is_palindromic to allow checks on different sections of a string.
	input: 
			word: something that can be made into a string
			start: the index of the first character to be tested
			len: the length of the string to be tested.
	output: Boolean
	'''
	s = str(word)[start:start+len]
	return s == s[::-1]


def cartalk2_check(i):
	'''checks for palindromes satisfying cartalk2 in integer i
	''' 
	return (has_palindrome(i, 2, 4) and
			has_palindrome(i+1, 1, 5) and
			has_palindrome(i+2, 1, 4) and 
			has_palindrome(i+3, 0, 6))


def cartalk2_display():
	result = []
	for i in range(100000, 999999):
		if cartalk2_check(i):
			result.append(i)
	return result

print cartalk2_display()

