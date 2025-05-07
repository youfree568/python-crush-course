def read_files(filenames):
	"""Try to read text files"""
	for filename in filenames:
		print(f"\nFile {filename}")	
		try:
			with open(filename) as f:
				readed = f.read()
		except FileNotFoundError:
			pass
		else:
			print(readed)

read_files(["ext_files\\cats.txt", "text_files\\dogs.txt"])