from datetime import date

from utils import add, subtract

# Print name
print("Khandaker Saleh Mohammad Tajuddin")

# Print today's date
today = date.today()
print(today)

# Call add and subtract from utils
a = 10
b = 4
print(f"add({a}, {b}) = {add(a, b)}")
print(f"subtract({a}, {b}) = {subtract(a, b)}")
