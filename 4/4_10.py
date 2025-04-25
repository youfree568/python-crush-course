cubes = [i**3 for i in range(1, 11)]
for cube in cubes:
	print(cube)

print(cubes)

print("The first three item in the list are:")
print(cubes[:3])
print(len(cubes))
print("Three items from the middle of the list are:")
print(cubes[4:7])
print("The last three items in the list are:")
print(cubes[-3:])