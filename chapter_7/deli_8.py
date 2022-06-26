sandwich_orders = ['with_cheese','with ham', 'with chicken', 'with butter']
finish_sandwitches = []
while sandwich_orders:
	popped = sandwich_orders.pop()
	print(f"I made your sandwitch {popped}")
	finish_sandwitches.append(popped)
print(f"\nWe made sandwiches:")
for sandwich in finish_sandwitches:
	print(sandwich) 

    
