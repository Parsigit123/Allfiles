birth_date = input("Enter your birth year: ")
current_date = "20221224"

current_year = int(current_date[:4])
current_month = int(current_date[4:6])
current_day = int(current_date[6:])

birth_year = int(birth_date[:4])
birth_month = int(birth_date[4:6])
birth_day = int(birth_date[6:])

age_y = current_year - birth_year
age_m = current_month - birth_month
age_d = current_day - birth_day

print("You are: ", age_y, " years and", age_m, " months and", age_d, "days old.")

