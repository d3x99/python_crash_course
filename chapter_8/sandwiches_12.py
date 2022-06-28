def sandwich(*items):
	print("You ordered sandwich with:")
	for item in items:
		print(f'\t -' + item)

sandwich('ham', 'butter')
sandwich('strawberry jam', 'butter')
sandwich('peanut butter')