def make_car(
		manufacturer, model, **information):
	# taking information about car and store them in dictionary
	information["manufacturer"] = manufacturer.title()
	information["model"] = model.title()
	return information


car = make_car("Audi", "a4", color="silver", tow_package=True)
print(car)