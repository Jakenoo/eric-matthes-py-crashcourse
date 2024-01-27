text_messages = ['hello', 'hi', "what's up", 'bonjour', 'tfti', 'smelly']
# prints every item contained in a list
def show_messages(messages):
    for message in messages:
        print(message)
show_messages(text_messages)

sent_messages = []
# moves messages from one list to new list sent_messages
def send_messages(messages):
    while messages:
        index_message = messages.pop()
        sent_messages.append(index_message)

# send_messages(text_messages)
# print(text_messages)
# print(sent_messages)
        
# creating copy of text_messages and moving contents to sent_messages
send_messages(text_messages[:])
print(text_messages)
print(sent_messages)