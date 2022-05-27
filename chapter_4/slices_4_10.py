cubes = [value ** 3 for value in range(1,11)]
for cube in cubes:
	print(cube)

print('The first three items in the list are: ')
for cube in cubes[:3]:
	print(cube)

print('\n Three items from the middle are: ')
for cube in cubes[3:6]:
	print(cube)

print('\n The last three items in the list are:')
for cube in cubes[-3:]:
	print(cube)
