glossary = {
	'pep_8': 'Python Enhancment Proposal',
	'int': 'number without decimal points',
	'float': 'number with deciaml points',
	'control flow keywords': 'if, elif, else',
	'value keywords': 'None, True, False'
	}
print(f'I learned from previous lessons about: \n')
print(f"pep 8: {glossary.get('pep_8','none').title()}\n")
print(f"float: {glossary.get('float').title()}\n")
print(f"control flow keywords: {glossary.get('control flow keywords').title()}\n")
print(f"value keywords: {glossary.get('value keywords').title()}\n")