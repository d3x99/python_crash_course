cities = {
    'Krakow': {'country': 'Poland', 'population': '766k', 'fact': 'There are many monuments'},
    'Paris': {'country': 'France', 'population': '2161k', 'fact': 'PPl there dont care about their bumpers'},
    'Stockholm': {'country': 'Sweden', 'population': '975k', 'fact': 'There are many bridges'}
}

for city, keys in cities.items():
    print(f"\nCity name: {city}")
    for key, answer in keys.items():
        print(f"\t{key}: {answer}")