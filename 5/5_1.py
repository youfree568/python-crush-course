car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print(car != 'audi')
if car == 'subaru' or car == 'bmw':
	print(True)

if car == 'subaru' and car != 'bmw':
	print(True)

if 'subaru' in car:
	print(True)


print("\nIs car not 'subaru'? I predict False.")
print(car == 'Subaru')
print(car == 'audi')
if car == 'subaru' and car == 'bmw':
	print(True)
else:
	print(False)

if car.capitalize() != 'subaru':
	print(False)

if car.upper() not in 'subaru':
	print(False)