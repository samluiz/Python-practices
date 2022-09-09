from datetime import date

year = date.today().year

name = str(input("What's your name? "))
age = int(input("What's your age? "))

in_100_years = (year + 100) - age

print(f"When you turn 100 years old, the year will be {in_100_years}.")