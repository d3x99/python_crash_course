condition = "What is your age? \n"
age = 0
ppl = input("How many ppl? ")
person = 0
while person != int(ppl):
    age = input(condition)
    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age <= 12:
        print("The ticket is $10")
    else:
        print('The ticket is $16')
    person += 1 