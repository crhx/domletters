#!/usr/bin/env python3
import sys
	
# Lists and variables used in program
letter_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_score = 0
words = []

# Splits the input into a list of words
for line in sys.stdin:
	words += line.split()

# Examines each word if they only contain alphabetical characters
for word in words:
		for letter in word:
			if 91 > ord(letter.upper()) > 64:
				letter_counter[ord(letter.upper()) - ord('A')] += 1
			else:
				letter_counter = [0]*26
				break

# Examines the words letter count and appends the largest number to total score
		temp = 0
		for element in letter_counter:
			if element > temp:
				temp = element
		total_score += temp
		letter_counter = [0]*26

#Test case for swift.txt and sentence.txt
isinstance(total_score, int)

print("Total score was: ", end="")
print(total_score)

