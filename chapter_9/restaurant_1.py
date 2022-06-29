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


restaurant = Restaurant("u Pietrosa", "Highlander Bar")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()