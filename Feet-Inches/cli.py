from parser2 import parse
#from Feet-Inches.parser2 import parse
from Convert2 import convert


feet_inches = input("Enter feet and inches: ")


parsed = parse(feet_inches)
#print(parsed)
#result = convert(5, 12)
result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")






