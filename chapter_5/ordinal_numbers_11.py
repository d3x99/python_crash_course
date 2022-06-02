list_of_numb = []
for number in range(1,10):
	list_of_numb.append(number)
for number in list_of_numb:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")