class User:
	# class for user


	def __init__(self, first_name, last_name, date_of_birth, nickname):
		# few basic informations about the user
		self.first_name = first_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth
		self.nickname = nickname


	def describe_user(self):
		# cumulate all informations about user and print
		print("All information about the user: " +
			  "\nFirst name: " + self.first_name +
			  "\nLast name: " + self.last_name +
			  "\nDate of birth: " + self.date_of_birth +
			  "\nNickname: " + self.nickname)


	def greet_user(self):
		# printing personalized greetings
		print("Hello " + self.first_name.title() +
		      " we are glad you created the account in our service," +
		      " from now we will call you " + self.nickname.title())



user_1 = User("Bartek", "Slodyczka", "21.07.1998", "D3x69")
user_2 = User("Pawel", "Szymanski", "11.09.1998", "Noner")
user_3 = User("Random", "Randomiasty", "21.11.1960", "Random")

user_1.describe_user()
user_1.greet_user()
print("\n")
user_2.describe_user()
user_2.greet_user()
print("\n")
user_3.describe_user()
user_3.greet_user()
print("\n")
