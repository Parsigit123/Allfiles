print("Your country:")

while True:
    country = input("Which country are you from: ")
    country = country.strip()

    match country:
        case 'USA':
            print("Hello")
        case 'India':
            print("Namaste")
        case 'Germany':
            print("Hallo")
        case 'Iran':
            print("سلام")
        case 'exit':
            break
        case other:
            print("You entered an unknown command.")

print("Bye!")


