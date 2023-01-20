while True:
    try:
        width = float(input("Enter recatangle width: "))
        length = float(input("Enter recatangle length: "))

        if width == length:
#            exit("Thats lookos like a square.")
            print("Thats lookos like a square.")
#            exit()

        area = width * length
        print(area)


    except ValueError:
        print("Please enter a number.")

