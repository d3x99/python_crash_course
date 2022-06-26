condition = "What is your age? \n"
active = True
while active == True:
    age = input(condition)
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