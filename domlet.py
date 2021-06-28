import sys

set1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
words = []

for line in sys.stdin:
	words += line.split()
	print(words)
	
for word in words:
		print(word, end =" > ")
		for letter in word:
			if 91 > ord(letter.upper()) > 64:
				set1[ord(letter.upper()) - ord('A')] += 1
				for element in set1:
					print(element, end =", ")
				print('\n')
		set1 = [0]*26
