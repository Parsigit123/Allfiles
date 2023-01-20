def get_age(year_of_birth, cur_year=2022):
    age = cur_year - year_of_birth
    return age

year_of_birth = int(input("Input your birth year: "))
age = get_age(year_of_birth)
if age < 120:
    print("You are", age, "years old.")
else:
    print("Congratulations, you are more than 120 years old.")