class Restaurant:
	''' model of restaurant '''
	

	def __init__(self, restaurant_name, cuisine_type):
		# init name and cusine 
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		# describing restaurant
		print('This restaurant is called ' + self.restaurant_name + '.')
		print('Our cuisine type is ' + self.cuisine_type + '.')


	def open_restaurant(self):
		# inidicates that restaurant is open or not
		print("This restaurant is open")


my_restaurant = Restaurant("u Pietrosa", "Highlander Bar")
annie_restaurant = Restaurant("At Anna's", "Chinese food")
pawel_restaurant = Restaurant('Mr Pawel', "Polish")
darek_restaurannt = Restaurant('great Bar', "Mexican")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print('\n')
annie_restaurant.describe_restaurant()
pawel_restaurant.describe_restaurant()
darek_restaurannt.describe_restaurant()