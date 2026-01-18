import sys
from stats import num_of_words, num_of_chars_in_string, sort_dictionary


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()
	
def check_args():
	if len(sys.argv) < 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)

def main():
	check_args()
	text = get_book_text(sys.argv[1])
	char_dict = num_of_chars_in_string(text)
	sorted_list = sort_dictionary(char_dict)
	# print(text)

	#print(char_dict)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_of_words(text)} total words")
	print("--------- Character Count -------")
	for char in sorted_list:
		print(f"{char['char']}: {char['num']}")
	print("============= END ===============")

main()