def show_messages(messages):
	for message in messages:
		print(message)

def send_messages(messages, sent_messages):
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)



list_of_messages = ['Hey', 'Hello', 'Welcome', 'Hi']
list_of_sent_messages = []
send_messages(list_of_messages[:], list_of_sent_messages)
print(list_of_sent_messages)
print(list_of_messages)