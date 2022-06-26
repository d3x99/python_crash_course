print('Dream vacation poll\n')
results = {}
polling_active = True
while polling_active:
	name = input('Tell me your name.\n')
	dream_vac = input('If you could visit one place in the world, where would you go?\n')
	results[name] = dream_vac
	end_of_loop = input("Woould you like another person respond?(y/n)")
	if end_of_loop == 'n':
		polling_active = False
	else:
		continue
for name, respond in results.items():
	print(f"{name.title()} wants to visit {respond} the most.")