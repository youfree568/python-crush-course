filename = 'text_files\\aspasia.txt'

with open(filename, encoding='utf-8') as f:
	line = f.read()

print(f"'the' mentioned in book {line.count('the')} times.")
print(f"'The' mentioned in book {line.count('The')} times.")
print(f"'The ' mentioned in book {line.count('The ')} times.")
print(f"'the ' mentioned in book {line.count('the ')} times.")
print(f"'the' mentioned in book {line.lower().count('the')} times.")
print(f"'the ' mentioned in book {line.lower().count('the ')} times.")
print(f"'The ' mentioned in book {line.lower().count('The ')} times.")