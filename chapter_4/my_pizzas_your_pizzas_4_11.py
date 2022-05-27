fav_pizzas = ['pepperoni', 'capriciosa', 'with chicken']
friend_pizzas = fav_pizzas[:]
fav_pizzas.append('with argula')
friend_pizzas.append('with prosciutto')

for pizza in fav_pizzas:
	print('I like pizza  ' + pizza)


print('\n')

for pizza in friend_pizzas:
	print('My friend lika pizza  ' + pizza)

print('But after all, we love all kinds of pizza')

