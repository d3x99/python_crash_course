favorite_places = {
	'Bartek': ['Slodyczki', 'Zakopane', 'Krakow'],
	'Aneta' : ['Turkey', 'Bali', 'Tailhand'],
	'Dora': ['Slodyczki', 'Zakopane', 'Warsaw']
	
}
for name, favorite_place in favorite_places.items():
	print(f"\n{name} favorite places are:")
	for place in favorite_place:
		print(f"{place}")
