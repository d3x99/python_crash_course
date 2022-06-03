glossary = {
	'pep_8': 'Python Enhancment Proposal',
	'int': 'number without decimal points',
	'float': 'number with deciaml points',
	'control flow keywords': 'if, elif, else',
	'value keywords': 'None, True, False',
	'interpreted': 'Python is interpreted language',
	'key-function': 'items like min(), max(), sorted(), list.sort()',
	'list': 'build in python sequence',
	'list comprehension': 'compact way to process all items in a list, it looks like [for x in range(256) if x % 3 == 0]',
	'triple-quoted string': "used for strings with single and double quotations"
	}

for key, value in glossary.items():
	print(f"{key} meaning : {value}\n")