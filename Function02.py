# def greet():
#     message = "Hello"
#     new_message = message.capitalize()
#     print("Hej hey")
#     return new_message
#
#
# greeting = greet()
#
# print(len(greeting))

def greet(message):
    new_message = message.capitalize()
    print("Hej hey")
    return new_message

user_entry = input("Enter the message: ")
greeting = greet(user_entry)
print(greeting)
print(len(greeting))

