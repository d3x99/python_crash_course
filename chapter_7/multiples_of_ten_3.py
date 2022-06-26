number = input("Write a number ")
number = int(number)
if number % 10 == 0 and number >= 10:
    print(f'Number {number} is multiple of 10')
elif number <= 0:
    print('Enter positive number')
else:
    print(f'Number {number} is not multiple of 10')