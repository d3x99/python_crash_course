condition = "What is your age? \n"
condition2 = "Type 'quit' to escape \n"
while True:
    age = input(condition + condition2)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free")
        active = False
    elif age <= 12:
        print("The ticket is $10")
        active = False
    else:
        print('The ticket is 16')
        active = False