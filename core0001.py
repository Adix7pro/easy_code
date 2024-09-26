#gpt_bot
"""
just it talk with you
"""
from datetime import datetime

name = 'Adham'
age = 20
year_own = int(input("Enter your year: "))
result = name + '   is  ' + str(age) + '    years old '
print(result)
print(type(result))
print(type(name))
print(type(age))
now_date = datetime.now()
n_year = now_date.year
print(n_year-year_own)

