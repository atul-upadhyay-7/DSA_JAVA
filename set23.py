# PRACTICAL-3
# AIM: A program that reads a text file and counts the number of words in it.


def count(path):
	try:
		with open(path, 'r') as file:
			file_content = file.read()
		words = file_content.split()
		return f"data = {words}\nlength of the words: {len(words)}"
	except FileNotFoundError:
		return "Please provide valid file path."


path = "example.txt"
print(count(path))
