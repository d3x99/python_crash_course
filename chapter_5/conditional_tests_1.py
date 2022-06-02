name = 'Bartek'
print('Is name == "Bartek", I predict True')
print('Bartek' == name,'\n')

print('Is name == "bartek", I predict False')
print('bartek' == name,'\n')

print('Is name.lower() == "bartek", I predict True')
print('bartek' == name.lower(),'\n')

print('Is name == "bartek.title()", I predict True')
print('bartek'.title() == name,'\n')

print('Is name != "Bartek", I predict False')
print('Bartek' != name,'\n')

print('Is name != "bartek", I predict True')
print('Bartek' != name,'\n')

print('Is Btek not in "Bartek", I predict True')
print('Btek' not in name,'\n')

print('Is k not in "Bartek", I predict False')
print('k' not in name,'\n')


print('Is 22 == 22.1, I predict False')
print(22 == 22.1,'\n')

print('Is 22 == int(22.1), I predict True')
print(22 == int(22.1),'\n')

print('Is 22 != 22, I predict False')
print(22 != 22,'\n')

print('Is 21 != 22, I predict True')
print(21 != 21,'\n')

print('Is 21 < 22, I predict True')
print(21 < 22,'\n')

print('Is 21 > 22, I predict False')
print(21 > 22,'\n')

print('Is 22 >= 22, I predict True')
print(22 >= 22,'\n')

print('Is 22 <= 22, I predict True')
print(22 <= 22,'\n')

name1 = 'Ciotka'
print('Bwed' or 'idassd' in name1)

#it works when you input letter which are next to eachother or single letters
print('Is letter " " in "Bartek", I predict False')
print(' ' in name,'\n')

print('Is letter B in "Bartek", I predict True')
print('B' in name,'\n')

#it does not work properly i still dont why
# print('Is Bff and t in "Bartek", I predict False')
# print(('Bff' and 't') in 'Bartek','\n')
#print('Is B or c in "Bartek", I predict True')
#print('B' or 't' in name,'\n')

print('Is letter B in "Bartek", I predict True')
print('B' in name,'\n')

print('Is 22 >= 23 or 22 == 23, I predict False')
print(22 >= 23 or 22 == 23,'\n')

print('Is 22 >= 23 and 22 == 23, I predict False')
print(22 >= 23 and 22 == 23,'\n')

print('Is 22 <= 23 or 22 == 23, I predict True')
print(22 <= 23 or 22 == 23,'\n')

print('Is 23 >= 22 and 22 == 22, I predict True')
print(23 >= 22 and 22 == 22,'\n')

list_of_num = [2, 3, 4, 5]
print('i predict true ' + str(2 in list_of_num))

print('i predict true ' + str(6 not in list_of_num))
