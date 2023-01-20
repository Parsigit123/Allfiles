from typing import List

Waiting_list = ["sen", "ben", "john"]
Waiting_list.sort()

for index, item in enumerate(Waiting_list):
    item = item.title()
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

print("--------------")

H= "Hello".replace("o", "a")
print(H)

print("--------------")

Waiting_list.sort(reverse=True)
print(Waiting_list)

print("--------------")

filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    row2 = f"{index}-{item.title()}.txt"
    print(row2)

print("--------------")

ips = ['100.122.133.105', '100.122.133.111']
q = input("Enter the index of the IP you want: ")
print("You chose", ips[int(q)])

print("--------------")

menu = ["pasta", "pizza", "salad"]
for i, j in enumerate(menu):
    print(f"{i}.{j}")