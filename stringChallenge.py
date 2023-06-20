# Create a function that, given a string with at least three characters, returns an array of its:
#
# Length.
# First character.
# Last character.
# Middle character, if the string has an odd number of characters.
# Middle TWO characters, if the string has an even number of characters.

# Index of the second occurrence of the second character in the format "@ index #" and "not found" if the second character
# doesn't occur again.
#
#
# Examples
# allAboutStrings("LASA") ➞ [4, "L", "A", "AS", "@ index 3"]
#
# allAboutStrings("Computer") ➞ [8, "C", "r", "pu", "not found"]
#
# allAboutStrings("Science") ➞ [7, "S", "e", "e", "@ index 5"]


# functions that gets length, first and last character, middle character(s) and index
def allAboutStrings(string):
	# initialization
	middle_character = ''
	string_len = len(string)  # getting length of string
	new_array = []
	print("Printing string: " + string)

	# test whether the string is long enough
	if string_len < 3:
		print("The string given is not long enough.")

	# testing parity of strings and returns characters accordingly
	if string_len % 2 == 0:  # even length string, returns middle two characters
		middle_len = int(string_len / 2)
		middle_character = string[middle_len - 1] + string[middle_len]
	elif string_len % 2 == 1:  # odd length string, returns middle character
		middle_character = string[int(string_len / 2)]

	# getting second character and getting index
	index_of_sec_occurrence = string.find(string[1], 2)

	# Appending to array all values
	new_array.append(string_len)  # string length
	new_array.append(string[0])  # first character
	new_array.append(string[string_len - 1])  # last character
	new_array.append(middle_character)
	if index_of_sec_occurrence == -1:
		new_array.append("not found")
	elif index_of_sec_occurrence >= 0:
		at_index_append = "@ index " + str(index_of_sec_occurrence)
		new_array.append(at_index_append)

	# printing array
	print(new_array)


# calling function
allAboutStrings("LASA")
allAboutStrings("Computer")
allAboutStrings("Science")
