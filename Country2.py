
while True:
    user_action = input("Which country are you from: ")

    match user_action:
        case 'USA':
            print("Hello")
        case 'India':
            print("Namaste")
        case 'exit':
            break
        case other:
            print("You entered an unknown command.")

print("Bye!")