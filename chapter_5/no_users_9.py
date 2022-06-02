users = []
if users:
	for user in users:
		if user == 'admin':
			print(f"Hello {user}, would you like to see a status report")
		else:
			print(f"hello {user}")
else:
	print('We need to find users')