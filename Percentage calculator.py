while True:
    try:
        value = float(input("Enter value: "))
        total_value = float(input("Enter total value: "))
        if total_value == 0:
            print("Total value can not be zero.")
            continue

        percentage = (value / total_value) * 100
        print(f"That is {percentage}%")

    except ValueError:
        print("Please enter a number.")

