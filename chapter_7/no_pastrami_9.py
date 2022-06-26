sandwich_orders = ['with pastrami', 'with_cheese', 'with pastrami', 'with ham', 'with chicken', 'with butter', 'with pastrami']
finish_sandwitches = []
print('deli has run out of pastrami')
while 'with pastrami' in sandwich_orders:
	sandwich_orders.remove('with pastrami')
while sandwich_orders:
	popped = sandwich_orders.pop()
	print(f"I made your sandwitch {popped}")
	finish_sandwitches.append(popped)
print(f"\nWe made sandwiches:")
for sandwich in finish_sandwitches:
	print(sandwich) 

    
