import csv

while True:
    with open("weather.csv", 'r') as file:
        data = list(csv.reader(file))

    city = input("Enter a city: ")
    for row in data[1:]:
        if row[0] == city:
            print("Temperature in", row[0], "is", row[1], "degrees.")
