from idlelib.configdialog import is_int
from itertools import count

with open("words.txt", "r") as file:
	words = {}
	for line in file.readlines():
		words[line.strip()] = None

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def find_repeats(inp):
	res = {}
	counts = value_counts(inp)
	for letter in value_counts(inp).keys():
		if counts[letter] != 1:
			res[letter] = None
	return res

def add_counts(a, b):
	res = {}
	for letter in list(a.keys()) + list(b.keys()):
		if not letter in res.keys():
			subtotal = [0,0]
			if letter in a.keys():
				subtotal.append(a[letter])
			if letter in b.keys():
				subtotal.append(b[letter])
			res[letter] = sum(subtotal)
	return res




counter = value_counts('apple') #1(a,l,e) 2(p)
counter2 = value_counts('pineapple') #1(l,i,n,a) 2(e) 3(p)
# print(counter.get('z', 0))
# print(find_repeats(counter))
print(add_counts(counter, counter2))

def is_interlocking(word):
	a = word[0::2]
	b = word[1::2]
	if a in words.keys() and b in words.keys():
		# print(f"{word}: {a},{b}")
		return True

interlocking_words = []
# is_interlocking("schooled")
for word in words.keys():
	res = is_interlocking(word)
	if res:
		interlocking_words.append(word)

print(interlocking_words)

def has_duplicates(word):
	return len(find_repeats(word)) != 0

best = "unpredictably"
for word in words:
	if not has_duplicates(word) and len(word) > len(best):
		best = word
		print(best)
print(f"{best} is the longest present word with no repeating letters")
