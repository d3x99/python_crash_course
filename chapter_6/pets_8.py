pet_1 = {'kind of animal': 'dog', 'name_of_owner': 'Aneta', 'pet_name': 'Fisia'}
pet_2 = {'kind of animal': 'cat', 'name_of_owner': 'Slodyczki', 'pet_name': 'Kicia'}
pet_3 = {'kind of animal': 'snake', 'name_of_owner': 'Abdul', 'pet_name': 'Wisimulacha'}
pets = [pet_1, pet_2, pet_3]

for pet in pets:
	print(f"Kind: {pet['kind of animal']}\n"
		f"Name of owner: {pet['name_of_owner']}\n"
		f"Pet name: {pet['pet_name']}\n")
