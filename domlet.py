import sys

letter_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_score = 0
words = []

for line in sys.stdin:
	words += line.split()
	print(words)
	
for word in words:
		print(word, end =" > ")
		for letter in word:
			if 91 > ord(letter.upper()) > 64:
				letter_counter[ord(letter.upper()) - ord('A')] += 1
			else:
				letter_counter = [0]*26
				break

		temp = 0
		for element in letter_counter:
			if element > temp:
				temp = element
		print("scored: ", temp)
		total_score += temp
		letter_counter = [0]*26
		
print("Total score was: ", total_score)
