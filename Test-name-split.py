def pars_string(names):
    parsed = names.split(",")
    return len(parsed)

names = input("Enter names separated by commas (no space): ")
parsed2 = pars_string(names)
print(names)
print(parsed2)

