loop = True
while loop == True:
    topping = input('Input your pizza topping, quit to end \n')
    if topping != 'quit':
        print(f"You added {topping} to your pizza")
    else:
        loop = False