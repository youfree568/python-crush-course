a = 'hello'
b = 'Ok'
print('All True')
print(isinstance(a, str))
print(type(a) is str)
print(type(b) is not int)
print(a == 'Hello'.lower())
print(15 > 14)
print(15 < 16)
print(15>=15)
if 15 == 10 or 15>=9:
	print(True)
else:
	print(False)

if 'Ok' in b:
	print(True)

if 'b' not in b:
	print(True)

print('\nAll False')
print(isinstance(9, str))
print(type(a) == int)
print(b.lower == 'Ok')
print(15<=13)
if 15>11 and 15>16:
	print(True)
else:
	print(False)

	
