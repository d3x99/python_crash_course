def profile(name, surname, **user_info):
	#taking information about user and store them in a dictionary
	user_info['Name'] = name
	user_info['Surname'] = surname
	return user_info


user1 = profile("Bartek", "Slodyczka",
				Location="Nowe Bystre",
				Hobbies="Gry video",
				Sex="Male")
print(user1)