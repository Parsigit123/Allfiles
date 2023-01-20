filenames = ['1.doc', '1.report', '1.presentation']


# for filename in filenames:
#    filename = filename.strip('1.')
#    filename = f"1-{filename}.txt"

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)

#    file = open(f"files/{filename}", 'w')
#    file.write("-")
#    file.close()

print("---------------")

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

print("---------------")

usernames = ["john 1990", "alberta1970", "magnola2000"]
LL = [len(name) for name in usernames]
print(LL)

print("---------------")

user_entries = ['10', '19.1', '20']
user_numbers = [float(siffra) for siffra in user_entries]
print(sum(user_numbers))

print("---------------")

temperatures = [10, 12, 14]
temperatures = [str(item) + '\n' for item in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)

print("---------------")

numbers = [10.1, 12.3, 15.7]
numbers = [int(item) for item in numbers]
print(numbers)


