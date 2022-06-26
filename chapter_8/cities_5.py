def describe_city(city, country = 'poland'):
	print(f"{city.title()} is in {country.title()}.")

describe_city('Krakow')
describe_city('Warszawa')
describe_city('paris', 'france')