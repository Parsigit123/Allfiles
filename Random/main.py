import random


while True:
    lb = int(input("Enter the lower band: "))
    ub = int(input("Enter the upper band: "))
    ran = random.randint(lb, ub)
    print(ran)
