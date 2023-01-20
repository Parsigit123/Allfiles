def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    ave_local = sum(values) / len(values)
    return ave_local


average = get_average()
print(average)
