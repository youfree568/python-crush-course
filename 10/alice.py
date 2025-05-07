def count_words(filename):
	"""counting approximate number of words in books"""
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		pass
		# print("Your file don't find or does not exist.")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['text_files\\alice.txt', 'text_files\\siddhartha.txt', 'mobi_dick.txt']
for filename in filenames:
	count_words(filename)