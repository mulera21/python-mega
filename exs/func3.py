def greeting(message):
    new_message = message.capitalize()
    print("hey hey")
    return  new_message


user_entry = input("what greetings do you want")
greets = greeting(user_entry)
print(greets)