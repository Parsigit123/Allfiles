while True:
    try:
        waiting_list = ["john", "marry"]
        name = input("Enter name: ")

#   for i, item in enumerate(waiting_list):
#      if item == name:
        number = waiting_list.index(name)
        print(f"{name}'s turn is {number + 1}")
#       else:
#           print("The entered name is not in the list.")
    except ValueError:
        print(f"{name} is not in the list.")

