while True:

    password = input("Enter the password: ")

    result = {}

    if len(password) >= 8:
        result["Length"] = True
    else:
        result["Length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["upper-case"] = uppercase

 #   if all(result) == True:
    if all(result.values()):
        print("Strong Password.")
        break
    else:
        print("Weak Password.")




