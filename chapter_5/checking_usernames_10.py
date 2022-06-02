current_users = ['admin', 'BARTEK', 'aneta', 'goska', 'dorota']
current_users_lower = []
new_user = ['admiN', 'Bartek', 'ania', 'maciek', 'beata']
#making another list with low capitalized
for user in current_users:
	current_users_lower.append(user.lower())

for user in new_user:
	if user.lower() in current_users_lower:
		print(f'The name {user.title()} is already taken, choose anoter one')
	else:
		print(f'Username {user.title()} is available')

