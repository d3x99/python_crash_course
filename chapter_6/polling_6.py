favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'pyton'
}
#list contains ppl who should take pool
favorite_language_poll = ['annie', 'sarah', 'jen', 'christopher']

for person in favorite_language_poll:
	if person in favorite_language:
		print(f'Thank you {person.title()} for your responding, but you already taken the poll')
	else:
		print(f'We inviting you {person.title()} to take our poll')