def num_of_words(text):
	return len(text.split())

def num_of_chars_in_string(book_string):
	char_list = list(book_string.lower())
	char_dictionary = {}
	for char in char_list:
		if char not in char_dictionary:
			char_dictionary[char] = 1
		else:
			char_dictionary[char] += 1
	return char_dictionary

def sort_on(items):
	return items["num"]

def sort_dictionary(dict):
	list_dict = []
	# modified_dict = {}
	for char in dict:
		if char.isalpha(): # to ignore non alphanumeric chars
			list_dict.append({"char": char, "num": dict[char]})
	# Python doesn't can't sort dictionaries directly SO
	# sort_on is returning the value of "num" eg:
	#   sort_on({"char": "a", "num": 5}) → 5
	#   sort_on({"char": "b", "num": 2}) → 2
	#   sort_on({"char": "c", "num": 8}) → 8
	list_dict.sort(reverse=True, key=sort_on)
	return list_dict
