fav_numbers = {
	'Bartek': [3, 33],
    'Aneta': [7, 17, 2],
    'Dorota': [9, 32, 11, 5],
    'Pawel': [13],
    'Damian': [8, 1]
    }

for name, numbers in fav_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name} favorite number is:")
    else:
        print(f"\n{name} favorite numbers are:")
    for  number in numbers:
        print(number)