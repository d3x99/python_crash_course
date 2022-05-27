#ppl who i want to invite
guest_list = ['Mama', 'Pawel Szymanski', 'Aneta Budzyk', 'Damian']
print('I invite you ' + guest_list[0] + ' to a dinner in my house')
print('I invite you ' + guest_list[1] + ' to a dinner in my house')
print('I invite you ' + guest_list[2] + ' to a dinner in my house')
print('I invite you ' + guest_list[3] + ' to a dinner in my house')
#remove guest who cant make it and store which one
removed = guest_list.pop(0)
print("\nI'm sorry but " + removed + " can't make it bcs she's dead")

#replacing guest
guest_list.insert(0, 'Tata')
print('\nI invite you ' + guest_list[0] + ' to a dinner in my house')
print('I invite you ' + guest_list[1] + ' to a dinner in my house')
print('I invite you ' + guest_list[2] + ' to a dinner in my house')
print('I invite you ' + guest_list[3] + ' to a dinner in my house')
