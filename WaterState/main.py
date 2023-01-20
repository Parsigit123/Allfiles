while True:

    from function import state

    temp = float(input("Enter the temperature of the water: "))

    st = state(temp)
    print("The state of the water is: ", st)